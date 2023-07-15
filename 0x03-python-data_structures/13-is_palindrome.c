#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer
 * Return: 1 if it's a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *prev;
	listint_t *temp;

	slow = *head;
	fast = *head;
	prev = NULL;
	if (*head == NULL)
	{
		return (1);
	}
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}
	if (fast != NULL)
	{
		slow = slow->next;
	}
	while (slow != NULL)
	{
		if (prev->n != slow->n)
		{
			return (0);
		}
		prev = prev->next;
		slow = slow->next;
	}
	return (1);
}
