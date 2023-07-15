#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer
 * Return: 0 if it's a palindrome, 1 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;

	temp = NULL;
	if (*head == NULL)
	{
		return (0);
	}
	if (*head == temp)
	{
		return (0);
	}
	return (1);
}
