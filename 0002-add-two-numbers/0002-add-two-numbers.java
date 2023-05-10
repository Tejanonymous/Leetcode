/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head=null;
        
        int c=0;
        
        while(l1!=null && l2!=null)
        {
            ListNode temp=head;
            ListNode n=new ListNode(((l1.val+l2.val+c)%10));
            
            c=(l1.val+l2.val+c)/10;
            
            if(head==null)
                head=n;
            else{
            while(temp.next!=null)
                temp=temp.next;
            temp.next=n;    
                
            }
            System.out.print(l1.val);
            System.out.print(l2.val);
            
            System.out.println(c);
            
            l1=l1.next;
            l2=l2.next;
        }
        
        
        
        while(l1!=null || l2!=null)
        {
            if(l1!=null)
            {
               
                while(l1!=null)
                {
                    ListNode temp=head;
                    ListNode n=new ListNode((l1.val+c)%10);
                    
                    c=(l1.val+c)/10;
                    
                    
                    if(head==null)
                        head=n;
                    else
                    {
                        while(temp.next!=null)
                            temp=temp.next;
                        temp.next=n;
                    }
                    l1=l1.next;
                }
                    
            }
            else if(l2!=null)
            {
                while(l2!=null)
                {
                    ListNode temp=head;
                    ListNode n=new ListNode((l2.val+c)%10);
                    
                    c=(l2.val+c)/10;
                    
                    
                    if(head==null)
                        head=n;
                    else
                    {
                        while(temp.next!=null)
                            temp=temp.next;
                        temp.next=n;
                    }
                    l2=l2.next;
                }
                
            }
        }
            
            if(c!=0)
            {
                ListNode temp=head;
                ListNode n=new ListNode(c);
                while(temp.next!=null)
                    temp=temp.next;
                temp.next=n;
            }
        
        
        return head;
        
    }   
   }
 /*  */
