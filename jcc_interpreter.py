import json
import sys

def s(_):
    return '"' + _ + '"'

def i(_):
    return str(_)

def b(_):
    if _:
        return "true"
    else:
        return "false"

def enc(typ, val):
    if typ == "int":
        return i(val)
    elif typ == "string":
        return s(val)
    elif typ == "bool":
        return b(val)
    elif typ == "variable":
        return val

def inst_decl(decl):
    code_str = ""
    if decl['declare'] == "variable":
        code_str += decl['type'] + " " + decl['name']
        if 'value' in decl:
            code_str += " = " + enc(decl['type'], decl['value']) + ";"
        else:
            code_str += ";"
    elif decl['declare'] == "function":
        code_str += interpret_function(decl)
    elif decl['declare'] == "array":
        code_str += decl['type'] + " " + decl['name'] + "[] = {"
        if 'value' in decl:
            if decl['type'] == "int":
                for element in decl['value']:
                    code_str += i(element) + ", "
            elif decl['type'] == "string":
                for element in decl['value']:
                    code_str += s(element) + ", "
            elif decl['type'] == "bool":
                for element in decl['value']:
                    code_str += b(element) + ", "
            code_str = code_str[:len(code_str) - 2]
        code_str += "};"
    elif decl['declare'] == "object":
        code_str += interpret_object(decl)
    return code_str

def inst_call(inst):
    code_str = inst['call'] + "("
    if inst['parameters']:
        for param in inst['parameters']:
            code_str += enc(list(param.keys())[0], param[list(param.keys())[0]]) + ", "
        code_str = code_str[:len(code_str) - 2]
    code_str += ");"
    return code_str

def inst_print(inst):
    code_str = "cout << std::boolalpha << "
    for param in inst['print']:
        code_str += enc(list(param.keys())[0], param[list(param.keys())[0]])
        code_str += " << "
    code_str = code_str[:len(code_str) - 4]
    code_str += ";"
    return code_str

def inst_if(inst):
    code_str = "if ("
    if inst['if'] == "true":
        code_str += enc(list(inst['expression'][0].keys())[0], inst['expression'][0][list(inst['expression'][0].keys())[0]]) + ") {"
    elif inst['if'] == "false":
        code_str += "!" + enc(list(inst['expression'][0].keys())[0], inst['expression'][0][list(inst['expression'][0].keys())[0]]) + ") {"
    else:
        code_str += enc(list(inst['expression'][0].keys())[0], inst['expression'][0][list(inst['expression'][0].keys())[0]])
        code_str += f" {inst['if']} "
        code_str += enc(list(inst['expression'][1].keys())[0], inst['expression'][1][list(inst['expression'][1].keys())[0]])
        code_str += ") {"
    for _inst in inst['instructions']:
        code_str += interpret_instruction(_inst)
    code_str += "}"
    if "else" in inst:
        code_str += "else {"
        for inst in inst['else']:
            code_str += interpret_instruction(inst)
        code_str += "}"
    return code_str

def interpret_instruction(inst):
    code_str = ""
    if "import" in inst:
        code_str += interpret_import(inst)
    elif "declare" in inst:
        code_str += inst_decl(inst)
    elif "call" in inst:
        code_str += inst_call(inst)
    elif "print" in inst:
        code_str += inst_print(inst)
    elif "if" in inst:
        code_str += inst_if(inst)
    return code_str

def interpret_function(func):
    code_str = ""
    code_str += func['return'] + " " + func['name'] + "("
    if 'parameters' in func:
        for param in func['parameters']:
            code_str += param[list(param.keys())[0]] + " " + (list(param.keys())[0])
            code_str += ", "
        if len(func['parameters']):
            code_str = code_str[:len(code_str) - 2]
    code_str += ") {"
    if not func['instructions']:
        code_str += "}"
        return code_str
    for inst in func['instructions']:
        code_str += interpret_instruction(inst)
    code_str += "}"
    return code_str

def interpret_object(obj):
    code_str = ""
    code_str += "class " + obj['name'] + "{"
    if 'private' in obj:
        code_str += "private:"
        for inst in obj['private']:
            code_str += interpret_instruction(inst)
    if 'public' in obj:
        code_str += "public:"
        for inst in obj['public']:
            code_str += interpret_instruction(inst)
    code_str += "};"
    return code_str

def interpret_import(imp):
    importfile = open(imp['import'])
    importjson = json.load(importfile)
    code_str = interpret_json(importjson)
    return code_str

def interpret_json(src):
    code_str = ""
    for element in src:
        code_str += interpret_instruction(element)
    return code_str


if __name__ == "__main__":
    #dir = "examples/"
    # sourcefile = open(dir + 'code.json')
    # source = json.load(sourcefile)
    # destinationfile = open(dir + "code.cpp", "w")

    sourcefile = open(sys.argv[1])
    source = json.load(sourcefile)
    destinationfile = open(sys.argv[2], "w")
    code = "#include <stdio.h>\n" \
           "#include <stdlib.h>\n" \
           "#include <iostream>\n" \
           "#include <time.h>\n" \
           "using namespace std;\n" \
           "void randseed() {srand(time(0));}\n" \
           "int randrange(int min, int max) {return rand() % (max + 1 - min) + min;}\n"
    code += interpret_json(source)
    destinationfile.write(code)



