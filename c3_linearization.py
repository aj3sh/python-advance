"""
Example is taken from ExampleClass objects
This is just a example of C3 Linearization algorithm for understanding, not optimized.
"""
from typing import List


class ExampleClass:
    def __init__(self, name, *bases):
        self.name = name
        self.bases = bases

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def linearization(self):
        '''
        L[ A(B1, B2, B3, ..., BN) ] = A + merge(L[B1]), L(B2), L(B3), ..., L(BN), B1 B2 B3 ... BN )
        L[object] = object
        HEAD: B1
        TAIL: B2, B3, ..., BN
        GOOD HEAD: if head is not in the tail of any other lists
        '''
        if len(self.bases) == 0:
            return [self]
        
        return [self] + self.merge(
            [base.linearization() for base in self.bases] + [list(self.bases)]
        )

    def merge(self, merge_list):
        '''
        STEPS:
        1. Take the head of the first list
        2. If this head is good head then add it to the linearization of A
         and remove all from the list in the merge
        Otherwise, look at the head of the next list and take it if it is a good head.
        3. Then repeat the operation until all the classes are removed or it is impossible
         to find a good head (will raise an exception)
        '''
        mro_list = []
        i = 0
        while i < len(merge_list):
            bad_head_index = set()
            head = merge_list[i][0]

            j = 0
            # checking if head is good head (not in the tail of other list)
            while j < len(merge_list):
                l = merge_list[j]

                if head in l[1:]:
                    # head is not a good head
                    
                    # checking if conflict
                    if i in bad_head_index:
                        raise Exception(f'Error generating MRO {merge_list}')
                    bad_head_index.add(i)

                    # taking next first as a head
                    head = merge_list[j][0]
                    
                    # resetting loop
                    i = j
                    j = 0
                    continue
                    
                j += 1
            
            # taking good head
            good_head = merge_list[i][0]

            # removing good head from all lists
            for l in merge_list:
                if good_head in l:
                    l.remove(good_head)

            # filtering empty list
            merge_list = [l for l in merge_list if len(l) > 0]

            # adding to mro list
            mro_list.append(good_head)
            
            # resetting index
            i = 0

        return mro_list

    @property
    def mro(self):
        return self._mro

O = ExampleClass('O')
A = ExampleClass('A', O)
B = ExampleClass('B', O)
C = ExampleClass('C', O)
D = ExampleClass('D', A, B)
E = ExampleClass('E', B, C)
F = ExampleClass('F', D, E)

print(F.linearization())

# L[ A(O) ] 
# = A + merge(L(O), O)
# = A + merge(O, O)
# = A + O
# = AO

# L[ B(O) ] = BO
# L[ C(O) ] = CO

# L[ D(A, B) ] 
# = D + merge(L[A], L[B], AB)
# = D + merge(AO, BO, AB)
# = D + A merge(O, BO, B)
# = D + A + B + merge(O, O)
# = D + A + B + O
# = DABO

# L[ E(B, C) ]
# = E + merge(L[B], L[C], BC)
# = E + merge(BO, CO, BC)
# = E + B + merge(O, CO, C)
# = E + B + C + merge(O, O)
# = E + B + C + O
# = EBCO

# L[ F(D, E) ]
# = F + merge(L[D], L[E], DE)
# = F + merge(DABO, EBCO, DE)
# = F + D + merge(ABO, EBCO, E)
# = F + D + A + merge(BO, EBCO, E)
# = F + D + A + E + merge(BO, BCO)
# = F + D + A + E + B + merge(O, CO)
# = F + D + A + E + B + C + O
# = FDAEBCO


O = ExampleClass('O')
A = ExampleClass('A', O)
B = ExampleClass('B', O)
C = ExampleClass('C', A, B)
D = ExampleClass('D', B, A)
E = ExampleClass('E', C, D)
try:
    print(E.linearization())
except Exception as e:
    print(e)
# L[C(A,B)] = CABO
# L[D(B,A)] = DBAO
# L[E(C,D)] = E + merge( L[C], L[D], CD)
# = E + merge(CABO, DBAO, CD )
# = E + C + merge(ABO, DBAO, DO)
# = E + C + D + merge(ABO, BAO) # Conflict