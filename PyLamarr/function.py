def function(f):
    def wrap_f(db):
        import SQLamarr
        return SQLamarr.PyTransformer(db)(f)

    return wrap_f


def method(f):
    def wrap_f(s, db):
        import SQLamarr
        return SQLamarr.PyTransformer(db)(lambda db: f(s, db))

    return wrap_f

