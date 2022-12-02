#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the beginning of the node
 * @number: number to be inserted
 * Return: address of the new node, NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number);
{
	listintt_t *temp, *new;

	if (head == NULL)
	{
		return (NULL);
	}
	temp = *head;

	new  = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (temp->n > number)
	{
		*head = new;
		new->next = emp;
	}
	while (temp->next != NULL)
	{
		if (temp->next->n > number)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	return (new);
}
