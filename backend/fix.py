import pathlib
c = pathlib.Path("backend/models.py").read_text("utf-8-sig")
c = c.replace('                return "\\n"', '        return "\\n"')
pathlib.Path("backend/models.py").write_text(c, "utf-8")
import ast
ast.parse(c)
print("FIXED OK")
