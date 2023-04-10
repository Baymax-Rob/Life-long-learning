#include "cs50.h"
#include <stdio.h>
#include <string.h>
// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
// Addational
bool cycle(int winner, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // TODO:Recall that ranks[i] here represents the user¡¯s ith preference.
    for (int i = 0; i < candidate_count; i++)
    {
        // If name is a match for the name of a valid candidate
        if (strcmp(candidates[i], name) == 0) // strac
        {
            // voter has the candidate as their rank preference
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    // TODO:preferences[i][j] should represent the number of voters who prefer candidate i over candidate j.
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            // update the global preferences array to add the current voter¡¯s preferences.
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    // TODO: preferences[i][j] should represent the number of voters who prefer candidate i over candidate j.
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            // // update the global variable pair_count to be the number of pairs of candidates
            int a = preferences[i][j];
            int b = preferences[j][i];
            if (a > b)  // prefer candidate i over candidate j.
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;   // the number of pairs of candidates.
            }
            else if (a < b) // prefer candidate j over candidate i.
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // TODO
    int index;
    for (int i = 0; i < pair_count; i++) // i :number of pairs of candidates
    {
        int max = 0;
        // find max preferences and record corresponding to index
        for (int j = i; j < pair_count; j++)
        {
            if (max < preferences[pairs[j].winner][pairs[j].loser])
            {
                max = preferences[pairs[j].winner][pairs[j].loser];
                index = j;
            }
        }
        // descending exchange max
        pair tmp = pairs[i];
        pairs[i] = pairs[index];
        pairs[index] = tmp;
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        //  create the locked graph, adding all edges in decreasing order of victory strength
        if (!cycle(pairs[i].winner, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            if (locked[j][i])
            {
                break;
            }
            else if (j == candidate_count - 1)
            {
                printf("%s\n", candidates[i]);
            }
        }
    }

    return;
}

bool cycle(int winner, int loser)
{
    // if it is a tie
    if (winner == loser)
    {
        return true;
    }

    // go through the pairs of candidates in order and ¡°lock in¡± each pair to the candidate graph
    for (int i = 0; i < candidate_count; i++)
    {
        // so long as locking in that pair does not create a cycle in the graph.
        if (locked[loser][i])
        {
            if (cycle(winner, i))
            {
                return true;
            }
        }
    }
    //  graph is complete, the source of the graph (the one with no edges pointing towards it) is the winner!
    return false;
}