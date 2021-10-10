# def some_obscure_function(a):
#     if type(a) == str:
#         r = {}
#         for s in a:
#             r[s] = r.get(s, 0) + 1
#         return r
#     else:
#         r = {}
#         for s in a:
#             for k,v in some_obscure_function(s).items():
#                 r[k] = r.get(k, 0) + v
#         return r

def ss(a):
    s = ""
    for k in a:
        if type(k) == str:
            s += k  # + " "
        else:
            s += ss(k)
    return s
def some_obscure_function(a):
    r = {}
    for s in ss(a):
        r[s] = r.get(s, 0) + 1
    return r



a = ["wow", ["waow", "1000-7", "wahoo", ["oh"], ["dead", ["inside"]]]]
result = some_obscure_function(a)
print(result)



