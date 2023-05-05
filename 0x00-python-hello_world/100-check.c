#include "lists.h"

/**
 * check_cycle - Function that checks if a singly linked list
 * has a cycle in it
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *new = list;

	while (head != NULL && new->next && new->next->next)
	{
		head = head->next;
		new = new->next->next;

		if (new == head)
		{
			return 1
		}
	}
	return 0
}
