# BIO Redux

Main Weakness:
- CARELESSNESS IN CODE 
- practice writing stress tests
- Written questions are now relatively easy
- Cannot find the bugs in the programs
- If I improve the quality of my coding, it should be perfect
- Both/either write less buggy code or debug more effectively

Strategy:
- leverage fast development time for programs
- use time to complete all written questions and check answers
- almost always use code to solve extended qs
- be careful with written questions

Checklist:
- rtq again
- are all variables reset
- are you testing all possiblities
- for first time, print program output to check if procedures are correct

- Programming questions:
    - test all edge cases
    - randomly generate test cases
    - reread question and see if every detail is implemented
- DP:
    - Actual dp is easy
    - reconstruction is hard
    - Template:
        ```
        import math 

        def num_configs(params):
            return configs under those params

        ans = ''
        while answer incomplete:
            covered = 0
            for every option
                if option valid:
                    if num_configs(valid option) + covered >= target:
                        target -= covered
                        ans += valid option
                        break
                    covered += num_configs(valid option)
        print(ans)
        ```
    - also, always use equal sign, usually works


 