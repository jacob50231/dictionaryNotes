import yaml
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--old')
parser.add_argument('--new')
parser.add_argument('--output')

args = parser.parse_args()
os.remove(args.output)

def isDifferent(dict1,dict2,it = 0,truth = False,*args):
    done = False
    if truth:
        return True
    if type(dict1)==dict and type(dict2)==dict:
        for key in dict2.keys():
            if truth:
                return True
            if key == 'enumDef':
                continue

            elif key == 'links':
                try:
                    for item in dict2[key][0]['subgroup']:
                        if type(item)==dict and item not in dict1[key][0]['subgroup']:
                            return True
                except Exception:
                    pass

            if key not in dict1.keys(): # New Keys
                return True

            if type(dict2[key])==list: # Executes if item in dictionary is a list
                if dict2[key]!=dict1[key]: # Only executes next section of code if two lists are unequal
                    return True


        for key in dict2.keys():# This is put down here for formatting issues
            if truth:
                return True
            if key == 'enumDef':
                continue
            if key not in dict1.keys(): # New Keys
                return True

            if type(dict2[key])==dict: # Recursion through nested Dictionaries
                truth = isDifferent(dict1[key],dict2[key],truth)
                if truth:
                    return True

def findDifferences(dict1,dict2,it = 0,*args):
    done = False
    if type(dict1)==dict and type(dict2)==dict:
        for key in dict2.keys():
            if key == 'enumDef' or key == '$ref':
                continue

            elif key == 'links':
                try:
                    for item in dict2[key][0]['subgroup']:
                        if type(item)==dict and item not in dict1[key][0]['subgroup']:
                            for item1 in dict1[key][0]['subgroup']:
                                if item['name']==item1['name']:
                                        findDifferences(item,item1)
                            else:
                                file.write('\t'*(it+1) + '* Changes made to `' + key + '`\n')
                                file.write('\t'*(it+2)+'* `'+item['name']+'` added to subgroup' + '\n')
                except Exception:
                    pass

            elif key not in dict1.keys(): # New Keys
                for arg in args:
                    if done==False:
                        file.write('\t'*(it) + '* Changes made to `' + arg + '`\n')
                        done = True
                file.write('\t'*(it+1) + '* New property: `' + key + '`\n')


            elif type(dict2[key])==list: # Executes if item in dictionary is a list
                if dict2[key]!=dict1[key]: # Only executes next section of code if two lists are unequal
                    for arg in args:
                        file.write('\t'*(it) + '* Changes made to `' + arg + '`\n')
                    if key != 'enum':
                        file.write('\t'*(it+1) + '* Changes made to `' + key + '`\n')
                    for item in dict2[key]:
                        if type(item)==dict: # Iterates through dictionaries nested in lists
                            findDifferences(dict1[key],dict2[key],it + 1,str(key))
                        elif item not in dict1[key]: # Checks for items in the new test
                            if key !='enum':
                                file.write('\t'*(it+2) + '* New Item: `' + item + '`\n')
                            else:
                                file.write('\t'*(it+1) + '* New permissable value: `' + item + '`\n')
                    for item in dict1[key]:
                        if item not in dict2[key]:
                            if key == 'enum':
                                file.write('\t'*(it+1) + '* Dropped Enumeration: `' + item + '`\n' )
                            else:
                                file.write('\t'*(it+2) + '* Dropped Item: `' + item + '`\n')


        for key in dict2.keys():# This is put down here for formatting issues
            if key == 'enumDef':
                continue
            elif key not in dict1.keys(): # New Keys
                continue

            elif type(dict2[key])==dict and dict2[key]!=dict1[key]: # Recursion through nested Dictionaries
                if done == False:
                    for arg in args:
                        file.write('\t'*it + '* Changes made to `' + arg +'`\n')
                findDifferences(dict1[key],dict2[key],it + 1,str(key))




os.listdir(args.new + '/gdcdictionary/schemas')
os.path.basename(args.new + '/gdcdictionary/schemas/exposure.yaml') in os.listdir(args.new + '/gdcdictionary/schemas')

for schema in os.listdir(args.new + '/gdcdictionary/schemas'):
    if schema[0]!='_' and schema[-2:]=='ml':
        newfilename = args.new + '/gdcdictionary/schemas/'+schema

        if os.path.basename(schema) in os.listdir(args.old + '/gdcdictionary/schemas/'):
            oldfilename =args.old + '/gdcdictionary/schemas/'+os.path.basename(schema)
            with open(oldfilename) as file:
                oldfile = yaml.load(file,Loader = yaml.FullLoader)
            with open(newfilename) as file:
                newfile = yaml.load(file,Loader = yaml.FullLoader)

            if isDifferent(oldfile,newfile)==True:
                with open(args.output,'a') as file:
                    file.write('* Altered `' + os.path.basename(newfilename[:-5]) + '` Entity\n')
                    findDifferences(oldfile,newfile)

        else:
            with open(args.output,'a') as file:
                file.write('* New Entity: `' + os.path.basename(newfilename[:-5]) + '`\n')
