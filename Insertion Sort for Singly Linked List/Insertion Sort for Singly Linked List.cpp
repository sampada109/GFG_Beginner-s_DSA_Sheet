  if(head_ref==NULL ||head_ref->next==NULL )
        return head_ref;
        Node *head=head_ref;
        Node *cur=head_ref;
        while(cur!=NULL)
        {
            while(head!=cur)
            {
                if(head->data>cur->data)
                {
                    int d=head->data;
                    head->data=cur->data;
                    cur->data=d;
                }
                head=head->next;
            }
            head=head_ref;
            cur=cur->next;
        }
        return head_ref;
