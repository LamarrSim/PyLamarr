import SQLamarr

def function(f):
  def wrap_f(db):
    return SQLamarr.PyTransformer(db)(f)

  return wrap_f

