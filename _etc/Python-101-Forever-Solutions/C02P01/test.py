a = [1]

if a:
    a = []
    try:
        a.pop()
    except:
        pass
    finally:
        print("Maybe I performed pop()")