/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* recursive_mergeTwoLists(ListNode* L1, ListNode* L2)
    {
        if (L1 == nullptr)
        {
            return L2;
        }
        if (L2 == nullptr)
        {
            return L1;
        }
        
        if (L1->val <= L2->val)
        {
            L1->next = recursive_mergeTwoLists(L1->next, L2);
            return L1;
        }
        else // (L1->val < L2->val)
        {
            L2->next = recursive_mergeTwoLists(L2->next, L1);
            return L2;
        }
        
    }
    
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        return recursive_mergeTwoLists(l1, l2);
    }
    
    
};