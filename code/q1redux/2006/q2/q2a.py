rule = input()
'''
keep going through rule until find operator or
'''
def test_simple(rule,password):
    for i in range(len(rule)):
        if rule[i]:
            pass
        elif rule[i] == "u":
            if password[i] > password[i-1]:
                pass
            else:
                return False
        elif rule[i] == "d":
            if password[i] < password[i-1]:
                pass
            else:
                return False
    return True

def gen_config(prefix,expression,operator):
    print(prefix,expression,operator)
    configs = []
    if operator == "*":
        for i in range(1,12):
            configs.append(prefix+expression*i)
    if operator == "?":
        configs.append(prefix)
        # ! prefix without expression
        configs.append(prefix[:-1])
    return configs
    

configs = []
config = ''

config = ''
for i in range(len(rule)):
    print(i)
    if rule[i] == "(":
        expression = ''
        for j in range(i+1,len(rule)):
            if rule[j] == ")":
                # print(expression)
                break
            expression += rule[j]
        operator = rule[j+1]
        configs += gen_config(config,expression,operator)
    elif rule[i-1] != ")" and (rule[i] == "*" or rule[i] == "?"):
        # print("WHAT")
        expression = rule[i-1]
        configs += gen_config(config,expression,rule[i])
    config += rule[i]
if not "?" in config and not "*" in config:
    configs.append(config)
print(configs)
        
    
        
        
    # config += rule[i]
        
        
    