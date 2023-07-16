#include "Python.h"
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about python lists
 * @p: pointer to PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *obj;

	obj = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", obj->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (i = 0; i < obj->ob_base.ob_size; i++)
	{
		printf("Element: %d: %s\n", i, obj->ob_item[i]->ob_type->tp_name);
	}
}
