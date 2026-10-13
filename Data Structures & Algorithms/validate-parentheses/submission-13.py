class Solution:
    def isValid(self, s: str) -> bool:

        # Translate close and open brackets for O(1) time
        bracket_map = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        # Create stack
        bracket_stack = []

        # Loop through strings for brackets
        for bracket in s:

            # Opening Bracket
            if bracket in bracket_map.values():

                # Add open bracket to stack
                bracket_stack.append(bracket)

            # Closing Bracket
            elif bracket in bracket_map.keys():

                # If bracket stack empty means closing bracket is first therefore false
                if bracket_stack == []:
                    return False

                # Pop open bracket compare to current closing bracket
                open_bracket = bracket_stack.pop()
                if bracket_map[bracket] != open_bracket:
                    return False 

        # if bracket stack, opening bracket without closing bracket
        if bracket_stack:
            return False

        return True



