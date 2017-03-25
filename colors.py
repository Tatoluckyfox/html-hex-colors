fil = open("colors.html", "w")

def ex(n):
    return '#' + str(hex(n)).split('x')[1]

fil.write("<html>\n <head>\n<title>HTML Hex colors</title>\n    </head>\n   <body>\n        <table>")
for x in range(1048576, 16777215):

    fil.write('         <tr>\n              <th>{name}</th><th style="background-color= {bg}; color: {fg}">This is the foreground with this background</th>\n           </tr>'.format(name=ex(x), bg=ex(x), fg=ex(x)) + '\n')
    
fil.write('     </table>\n      <a href="https://github.com/tatoluckyfox/html-hex-colors">github.com/tatoluckyfox/html-hex-colors</a>\n </body>\n</html>')
fil.close()
