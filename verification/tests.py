"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        { "input": [[1,3,3,4,2,4],
                    [2,3,4,1,1,3],
                    [1,2,1,3,4,2],
                    [2,4,2,1,1,4],
                    [4,3,2,1,4,3]],
          "answer":8
        },
        { "input": [[1,2,3,4,5],
                    [2,3,4,5,1],
                    [3,4,5,1,2],
                    [4,5,1,2,3],
                    [5,1,2,3,4]],
          "answer":0
        },
        { "input": [[4,3],
                    [3,4],
                    [4,3],
                    [3,4],
                    [4,3]],
          "answer":3
        },
        { "input": [[1,0,1],
                    [0,1,0],
                    [1,0,1]],
          "answer":4
        },
        { "input": [[1,4,5,2,2,3,2,2,5],
                    [1,1,4,4,1,2,3,3,1],
                    [2,4,1,3,1,4,5,1,1],
                    [1,5,5,1,3,3,2,4,2],
                    [3,2,2,4,1,3,3,5,5],
                    [2,1,4,5,3,1,1,4,2],
                    [2,3,1,4,2,1,3,4,3],
                    [5,1,5,3,4,3,4,1,2],
                    [1,2,5,5,4,3,3,4,2]],
          "answer":26
        },
    ]
}
