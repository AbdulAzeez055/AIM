def is_variable(expr):
    return isinstance(expr, str) and expr.islower()

def is_constant(expr):
    return isinstance(expr, str) and expr.isupper()

def occurs_in(var, expr):
    if var == expr:
        return True
    if isinstance(expr, list):
        return any(occurs_in(var, arg) for arg in expr)
    return False

def apply_substitution(subst, expr):
    if not subst:
        return expr
    if isinstance(expr, str):
        return subst.get(expr, expr)
    if isinstance(expr, list):
        return [apply_substitution(subst, arg) for arg in expr]
    return expr

def unify(psi1, psi2):
    if isinstance(psi1, str) or isinstance(psi2, str):
        if psi1 == psi2:
            return {}
        elif is_variable(psi1):
            if occurs_in(psi1, psi2):
                return "FAILURE"
            else:
                return {psi1: psi2}
        elif is_variable(psi2):
            if occurs_in(psi2, psi1):
                return "FAILURE"
            else:
                return {psi2: psi1}
        else:
            return "FAILURE"

    if psi1[0] != psi2[0]:
        return "FAILURE"

    if len(psi1) != len(psi2):
        return "FAILURE"

    subst = {}

    for i in range(1, len(psi1)):
        s = unify(psi1[i], psi2[i])
        
        if s == "FAILURE":
            return "FAILURE"
        
        if s != {}:
            psi1 = apply_substitution(s, psi1)
            psi2 = apply_substitution(s, psi2)
            
            for key in subst:
                subst[key] = apply_substitution(s, subst[key])
            subst.update(s)

    return subst
