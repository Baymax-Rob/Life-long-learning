#include "cs50.h"
#include <stdio.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // TODO: Recall that candidate_count stores the number of candidates in the election.
      for (int i = 0; i < candidate_count; i++)
    {
        // If name is a match for the name of a valid candidate,
        if (strcmp((candidates[i].name), name) == 0)
        {
            // update the global preferences array to indicate that the voter voter has that candidate as their rank preference
            // Recall that preferences[i][j] stores the index of the candidate who is the jth ranked preference for the ith voter.
            preferences[voter][rank] = i;
            // If the preference is successfully recorded, the function should return true
            return true;
        }
    }
    // the function should return false otherwise
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO: voter_count stores the number of voters in the election and that, for each voter in our election, we want to count one ballot.
    int j = 0;
    for (int i = 0; i < voter_count; i++)
    {
        // i, their top choice candidate is represented by preferences[i][0], their second choice candidate by preferences[i][1]
        int k = preferences[i][j];
        // candidate struct has a field called eliminated, which will be true if the candidate has been eliminated from the election.
        if (!candidates[k].eliminated)
        {
            // candidate struct has a field called votes, which you¡¯ll likely want to update for each voter¡¯s preferred candidate.
            candidates[k].votes++;
            // stop there, not continue down their ballot
            j = 0;
        }
        else
        {
            i--;
            j++;
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO: Traverse the election group to get the maximum number of votes, and record its subscript
    int maxVotes = 0; // mv = maximum votes
    int maxIndex; // mi = maximum index
    for (int i = 0; i < candidate_count; i++)
    {
        if (maxVotes < candidates[i].votes)
        {
            maxVotes = candidates[i].votes;
            maxIndex = i;
        }
    }

    int w = voter_count / 2;
    // If any candidate has more than half of the vote, their name should be printed and the function should return true.
    if (candidates[maxIndex].votes > w)
    {
        printf("%s\n", candidates[maxIndex].name);
        return true;
    }
    // If nobody has won the election yet, the function should return false
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    int minVotes = voter_count;
    for (int i = 0; i < candidate_count; i++)
    {
        if (minVotes > candidates[i].votes && !candidates[i].eliminated)
        {
            minVotes = candidates[i].votes;
        }
    }
    return minVotes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO:Screen the candidates with the minimum number of votes eliminated as true
    int nec = 0; // nem = non  eliminated candidates
    int c = 0; // c = count candidates with same minimum votes
    for (int i = 0; i < candidate_count; i++)
    {
        if (!candidates[i].eliminated)
        {
            if (candidates[i].votes == min)
            {
                c++;
            }
            nec++;
        }
    }

    if (nec == c)
    {
        //  return true if every candidate remaining in the election has the same number of votes,
        return true;
    }
    // return false otherwise
    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == min)
        {
            // The function should eliminate the candidate (or candidates) who have min number of votes.
            candidates[i].eliminated = true;
        }
    }
    return;
}