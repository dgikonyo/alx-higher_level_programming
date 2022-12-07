#include <lists.h>

/**
 * reverse_listint - reverse a linked list
 * @head: list to be checked
 *
 * Return - 0 if not a palindrome and 1 if its a palindrome
 */
int reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current){
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	
	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it's a palindrome, 0 if it's not
 */
int is_palindrome(listint_t **head)
{
	listint_t *
}
