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



        for bracket in s:

            print(bracket_stack)
            # Opening Bracket
            if bracket in bracket_map.values():

                # Add open bracket to stack
                bracket_stack.append(bracket)

            # Closing Bracket
            elif bracket in bracket_map.keys():

                if bracket_stack == []:
                    return False

                # Pop open bracket compare to current closing bracket
                open_bracket = bracket_stack.pop()
                if bracket_map[bracket] != open_bracket:
                    return False 

        if bracket_stack:
            return False
        return True



