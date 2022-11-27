def test():
    pass


method_code = "print('Hello world')"
code_obj = compile(method_code, '_', 'exec')

a = test.__class__(code_obj, globals())
a()
