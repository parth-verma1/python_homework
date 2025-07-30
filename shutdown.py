def shutdown(x):
    if x == "yes":
        print("shutting down")
    elif x == "no":
        print("abort shut down")
    else:
        print("sorry")

ans = input("type Yes or no: ")
shutdown(ans)
