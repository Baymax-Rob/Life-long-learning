#include "cs50.h"
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
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
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO:Iterate over the entire array of electors
    for (int i = 0; candidates[i].name != NULL; i++)
    {
        // stracsecmp:Determines whether strings are equal, ignoring case
        if (strcasecmp((candidates[i].name), name) == 0)
        {
            // If name matches one of the names of the candidates in the election, then update that candidate’s vote total to account for the new vote.
            // The vote function in this case should return true to indicate a successful ballot.
            candidates[i].votes++;
            return true;
        }
    }
    // If name does not match the name of any of the candidates in the election, no vote totals should change, and the vote function should return false to indicate an invalid ballot.
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // First, determine the maximum number of votes in the set of electors
    int max = 0;
    for (int i = 0; candidates[i].name != NULL; i++)
    {
        if (max <= candidates[i].votes)
        {
            max = candidates[i].votes;
        }
    }

    // Then confirm the corresponding elector according to the maximum number of votes
    for (int i = 0; candidates[i].name != NULL; i++)
    {
        if (candidates[i].votes == max)
        {
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}