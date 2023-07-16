#include "Python.h"
/**
 * print_python_list_info - prints some basic info about python lists
 * @p: pointer to PyObject
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element: %lu: %s\n", i, obj->ob_type->tp_name);
	}
}
