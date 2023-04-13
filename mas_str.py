# ALINEAR CADENAS

# center - cemtrar un str
titulo = 'Sitio Web de GlobalMentoring.com.mx'
#print(len(titulo))
#print(titulo.center(50,'*'))
print(titulo.center(len(titulo)+10, '*'))
print(titulo.ljust(len(titulo)+5, '-'))
print(titulo.rjust(len(titulo)+5, '-'))

# REMPLAZAR CONTENIDO EN UN STR
print(titulo.replace(' ', '-'))

# ELIMINAR CARACTERES AL INICIO Y AL FINAL ED UN STR
titulo = ' *** GloblaMentoring.com.mx ***'
titulo = titulo.strip()
print(titulo)

titulo = '***GloblaMentoring.com.mx***'.strip('*')
print(titulo)