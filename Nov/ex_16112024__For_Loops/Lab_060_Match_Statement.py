# # SYNTAX
# Match variable :
#     Case pattern 1
#       # code block
#     Case pattern 2
#       # code block

Browser_name = input("Enter the browser name\n")
match Browser_name:
    case "FireFox":
        print("Starting FireFox")
    case "Chrome":
        print("Starting Chrome")
    case "Edge":
        print("Starting Edge")
    case _:
        print("Browser not Found")