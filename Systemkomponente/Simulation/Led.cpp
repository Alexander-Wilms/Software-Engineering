/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Led
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Led.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Led.h"
//#[ ignore
#define System_Led_Led_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Led
Led::Led() {
    NOTIFY_CONSTRUCTOR(Led, Led(), 0, System_Led_Led_SERIALIZE);
}

Led::~Led() {
    NOTIFY_DESTRUCTOR(~Led, true);
}

bool Led::getOn() const {
    return On;
}

void Led::setOn(bool p_On) {
    On = p_On;
    NOTIFY_SET_OPERATION;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedLed::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("On", x2String(myReal->On));
}
//#]

IMPLEMENT_META_P(Led, System, System, false, OMAnimatedLed)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Led.cpp
*********************************************************************/
