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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = nullptr;
        bool carry_over = 0;
        recursive_solve(l1, l2, &result, carry_over);
        return result;
    }
    
    void InsertFront(ListNode** result, int value)
    {
        ListNode* new_node = new ListNode(value);
        new_node->next = *result;
        *result = new_node;
    }
    
    void helper(ListNode* long_list, ListNode** result, bool &carry_over)
    {
        if (long_list != nullptr)
        {
            int sum = long_list->val + carry_over;
            carry_over = sum / 10;
            sum = sum % 10; 
            helper(long_list->next, result, carry_over);
            InsertFront(result, sum); 
        }
        if (long_list == nullptr && carry_over == 1)
        {
            InsertFront(result, 1);
            return;
        }
    }
    void recursive_solve(ListNode* l1, ListNode* l2, ListNode** result, bool &carry_over)
    {
        if (l1 == nullptr && l2 == nullptr && carry_over == 1)
        {
            InsertFront(result, 1);
            return;
        }
        else if (l1 == nullptr && l2 != nullptr)
        {
            helper(l2, result, carry_over);
        }
        else if (l2 == nullptr && l1 != nullptr)
        {
            helper(l1, result, carry_over);
        }
        else if (l1 != nullptr && l2 != nullptr)
        {
            // l2 & l1 is not nullptr   
            int sum = l1->val + l2->val + carry_over;
            carry_over = sum / 10;
            sum = sum % 10;
            recursive_solve(l1->next, l2->next, result, carry_over);
            InsertFront(result, sum);
        }
        else
        {
            
        }
    }
    
    /*
        LinkedList
            * [ ] InsertFront
    */
};