"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['somefile.txt', '*'],
            "answer": True,
            "explanation": "* matches everything"
        },
        {
            "input": ['other.exe', '*'],
            "answer": True,
            "explanation": "* matches everything"
        },
        {
            "input": ['my.exe', '*.txt'],
            "answer": False,
            "explanation": "filename should ends with \".txt\" but \".exe\" found "
        },
        {
            "input": ['log1.txt', 'log?.txt'],
            "answer": True,
            "explanation": "? matches any single character (in this case it is \"1\""
        },
        {
            "input": ['log1.txt', 'log[1234567890].txt'],
            "answer": True,
            "explanation": "[seq] matches any character in seq. \"1\" is in \"1234567890\""
        },
        {
            "input": ['log12.txt', 'log?.txt'],
            "answer": False,
            "explanation": "? matches any single character. Not more than one"
        },
        {
            "input": ['log12.txt', 'log??.txt'],
            "answer": True,
            "explanation": "? matches any two character"
        }
    ],
    "Extra": [
        {
            "input": ['log12.txt', '**'],
            "answer": True,
            "explanation": "** works the same as *"
        },
        {
            "input": ['file19.txt', '*z*'],
            "answer": False,
            "explanation": "\"z\" should be somewhere inside the filename"
        },
        {
            "input": ['l.txt', '???*'],
            "answer": True,
            "explanation": "Filename should be 3 chars long"
        },
        {
            "input": ['txt', '????*'],
            "answer": False,
            "explanation": "Filename should be 4 chars long"
        },
        {
            "input": ['name.txt', 'name.txt'],
            "answer": True,
            "explanation": "filename matches itself"
        },
        {
            "input": ['name.txt', 'name.exe'],
            "answer": False,
            "explanation": "filename matches itself"
        },
        {
            "input": ['name.txt', 'name[.]txt'],
            "answer": True,
            "explanation": "seq with one character works the same as just a one char"
        },
        {
            "input": ['name.txt', 'name[]txt'],
            "answer": False,
            "explanation": "seq without any chars will never match"
        },
        {
            "input": ['nametxt', 'name[]txt'],
            "answer": False,
            "explanation": "seq without any chars will never match"
        },
        {
            "input": ['name.txt', '[!abc]name.txt'],
            "answer": False,
            "explanation": "[!seq] matches any character not in seq"
        },
        {
            "input": ['1name.txt', '[!abc]name.txt'],
            "answer": True,
            "explanation": "[!seq] matches any character not in seq"
        },
        {
            "input": ['1name.txt', '[!1234567890]*'],
            "answer": False,
            "explanation": "filename should not start with number"
        },
        {
            "input": ['name.txt', '[!1234567890]*'],
            "answer": True,
            "explanation": "filename should not start with number"
        },
        {
            "input": ['a1name.txt', '[!1234567890]*'],
            "answer": True,
            "explanation": "filename should not start with number"
        },
        {
            "input": ['apache12.log', '*[1234567890].*'],
            "answer": True,
            "explanation": "should be a number before extension"
        },
        {
            "input": ['apache.1log', '*[1234567890].*'],
            "answer": False,
            "explanation": "should be a number before extension"
        },
        {
            "input": ['apache1.log', '*.*'],
            "answer": True,
            "explanation": "filename should have an extension"
        },
        {
            "input": ['12apache1.log', '*.*'],
            "answer": True,
            "explanation": "filename should have an extension"
        },
        {
            "input": ['12apache1', '*.*'],
            "answer": False,
            "explanation": "filename should have an extension"
        },
        {
            "input": ['name.txt', 'name.???'],
            "answer": True
        },
        {
            "input": ['name.exe', 'name.???'],
            "answer": True
        },
        {
            "input": ['name....', 'name.???'],
            "answer": True
        },
        {
            "input": ['name....', 'name.*'],
            "answer": True
        },
        {
            "input": ['name....', 'name.[!.][!.][!.]'],
            "answer": False
        },
        {
            "input": ['name.exe', 'name.[!.][!.][!.]'],
            "answer": True
        },
        {
            "input": ['[!]check.txt', '[!]check.txt'],
            "answer": True,
            "explanation": "[!] is not class"
        },
        {
            "input": ['check.txt', '[[c]heck.txt'],
            "answer": True,
            "explanation": "unmatched brackets"
        },
        {
            "input": ['[?*]', '[[][?][*][]]'],
            "answer": True,
            "explanation": "escaping metacharacters"
        },
        {
            "input": ['Feb 2018', '[A-Z][a-z][a-zA-Z] [2-3][0-4][1-1][5-9]'],
            "answer": True
        },
        {
            "input": ['[check].txt', '[][]check[][].txt'],
            "answer": True
        },
        {
            "input": ["checkio", "[c[]heckio"],
            "answer": True
        },

    ]
}
