# BIO Redux

Strategy:
- leverage fast development time for programs
- use time to complete all written questions and check answers
- almost always use code to solve extended qs
- be careful with written questions
- checklist:
    - rtq again
    - are all variables reset
    - are you testing all possiblities
    - for first time, print program output to check if procedures are correct
- programming questions
    - test all edge cases
    - randomly generate test cases
    - reread question and see if every detail is implemented
- DP
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


 