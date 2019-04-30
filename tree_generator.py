import os
import re


def tree_generator(code):


    #code=re.sub("'''.*'''",'',code,flags=re.DOTALL).strip()
    #code=code.replace('"','')
    #code=code.replace("'","")
    function_stack={'null':[]}
    function_docstring={}
    function_names=[]
    curr_def = 'null'
    for line in code.splitlines():



        if 'def ' in line:
            curr_def=line.partition('def ')[2].partition('(')[0].strip()
            function_stack['%s'%curr_def]=[]
            function_names.append('%s'%curr_def)
        '''elif 'main()' in line or '__main__' in line:
            continue
        else:
            if '(' in line and ')':
                function_stack['%s'%curr_def].append(line)'''
    curr_def='null'
    f=''
    for line in code.splitlines():

        if 'def ' in line:

            function_docstring['%s'%curr_def]=f.partition("'''")[2].partition("'''")[0].strip()
            f=''
            curr_def = line.partition('def ')[2].partition('(')[0].strip()

        if '#' in line:
            if line.partition('#')[0].strip() is '':
                continue
        f += line + '\n'
        for fun_name in function_names:
            if '%s'%fun_name in line and line.partition(fun_name)[2].strip().partition('(')[0].strip() is '' :
                function_stack['%s'%curr_def].append(fun_name)
    function_docstring['%s' % curr_def] = f.partition("'''")[2].partition("'''")[0].strip()

    have_init=False
    for fun_name in function_names:
        if fun_name == '__init__':
            have_init=True

        elif fun_name in function_stack['%s'%fun_name]:
            function_stack['%s' % fun_name].remove(fun_name)
            function_stack['%s' %fun_name]=list(set(function_stack['%s' %fun_name]))


        '''if function_stack['%s'%fun_name] ==[] or len(fun_name) > 40:
            del function_stack['%s'%fun_name]'''
    del function_stack['null']
    del function_docstring['null']
    if have_init:
        del function_stack['__init__']






    return function_stack,function_docstring


def generate_diag(function_stack):
    s = 'blockdiag { '
    for function in function_stack:
        if not function_stack[function] is []:
            for i in function_stack[function]:
                s += ' '+ function + ' -> ' + i + ' ; '


            #else:
             #   s+=i+' -> '
    s+=' } '
    #f=open('./diag/%s.diag'%function,'w')
    f = open('./source/full.diag' , 'w+')
    f.write(s)
    f.close()
    print(" : "+s)
    os.system('blockdiag ./source/full.diag')
    f=open('./source/codeflow.rst','w+')
    f.write("CODEFLOW\n========\n   function flow in source code\n   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n.. image:: full.png")
    f.close()


def create_rst(function_stack,function_docstring):
    for function in function_stack:


        s=str(function)+'\n'+str(''.join(['=' for i in range(len(str(function)))]))
        if function_stack[function] is not []:
            s += '\nfunctional dependenies for ' + str(function) + ':\n' + str(
                ''.join(['^' for i in range(len(str(function)) + 28)])) + '\n'
        for i in function_stack[function]:

            s+="\t `"+str(i)+"() <"+str(i)+".html>`_ \n\n"

        s+="\n"+str(function)+"() description\n"+str(''.join(['^' for j in range(len(function)+14)]))+"\n\n\t"+function_docstring['%s'%function]+'\n\n'
        f=open('./source/%s.rst'%function,'w+')
        f.write(s)
        f.close()

        print(str(function)+":"+s)



if __name__=='__main__':
    if not os.path.exists('./source/conf.py'):
        os.system('sphinx-quickstart')
    f=open('./__init__.py','r').read()
    file_names=[]
    for line in f.splitlines():
        if 'from' in line and 'import' in line:
            file_names.append(line.partition('from')[2].partition('import')[0].strip()+'.py')

    del f
    f=''
    for file_name in file_names:
        f+=open('%s'%file_name,'r').read().partition('if __name__ ==')[0]+'\n'
    function_stack,function_docstring=tree_generator(f)
    print(function_docstring)
    print(function_stack)

    generate_diag(function_stack=function_stack)
    create_rst(function_stack=function_stack,function_docstring=function_docstring
                  )
    if os.path.exists('./source/index.rst'):
        f='''.. bag_packing documentation master file, created by
            sphinx-quickstart on Fri Apr 26 11:52:42 2019.
            You can adapt this file completely to your liking, but it should at least
            contain the root `toctree` directive.

Welcome to bag_packing's documentation!
=======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:\n\n   codeflow'''
        for function in function_stack:
            f+='''\n   %s'''%function
        f+='''\n\n\nIndices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
'''
        open('./source/index.rst','w').write(f)

