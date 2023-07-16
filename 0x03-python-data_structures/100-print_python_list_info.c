#include "Python.h"
/**
 * print_python_list_info - prints some basic info about python lists
 * @p: pointer to PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = PyList_Size(p);
	PyObject *q;
	Py_ssize_t allocated = ((PyListObject *)(p))->allocated;

	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", allocated);
	for (i = 0; i < size; i++)
	{
		q = PyList_GetItem(p, i);
		printf("Element: %lu: %s\n", i, q->ob_type->tp_name);
	}
}
