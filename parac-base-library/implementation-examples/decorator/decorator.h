/* Header for the decorator. Not necessarily required but in this case required for the example*/
#pragma once

#include "__parac__.h"

#ifndef DECORATOR_H
#define DECORATOR_H

/* If the code is included in an CPP environment which Para-C supports, it will be treated as regular C-code */
#if __cplusplus
extern "C" {
#endif

ph_ReturnTypeInt main_DecorateFunc_Wrapper(main_DecorateFunc_WrapContext*, int);
main_DecorateFunc_WrapContext DecorateFunc(main_DecorateFunc_WrapContext*);

#if __cplusplus
}
#endif

#endif