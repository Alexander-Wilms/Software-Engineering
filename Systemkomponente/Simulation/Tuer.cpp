/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Tuer
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Tuer.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Tuer.h"
//#[ ignore
#define System_Tuer_Tuer_SERIALIZE OM_NO_OP

#define System_Tuer_getZustand_SERIALIZE OM_NO_OP

#define System_Tuer_open_SERIALIZE OM_NO_OP

#define OMAnim_System_Tuer_setZustand_bool_UNSERIALIZE_ARGS OP_UNSER(OMDestructiveString2X,p_Zustand)

#define OMAnim_System_Tuer_setZustand_bool_SERIALIZE_RET_VAL
//#]

//## package System

//## class Tuer
Tuer::Tuer() : Zustand(1) {
    NOTIFY_CONSTRUCTOR(Tuer, Tuer(), 0, System_Tuer_Tuer_SERIALIZE);
}

Tuer::~Tuer() {
    NOTIFY_DESTRUCTOR(~Tuer, true);
}

bool Tuer::getZustand() {
    NOTIFY_OPERATION(getZustand, getZustand(), 0, System_Tuer_getZustand_SERIALIZE);
    //#[ operation getZustand()
    return Zustand;
    //#]
}

void Tuer::open() {
    NOTIFY_OPERATION(open, open(), 0, System_Tuer_open_SERIALIZE);
    //#[ operation open()
    Zustand = 0;
    //#]
}

void Tuer::setZustand(bool p_Zustand) {
    Zustand = p_Zustand;
    NOTIFY_SET_OPERATION;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedTuer::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("Zustand", x2String(myReal->Zustand));
}
//#]

IMPLEMENT_META_P(Tuer, System, System, false, OMAnimatedTuer)

IMPLEMENT_META_OP(OMAnimatedTuer, System_Tuer_setZustand_bool, "setZustand", FALSE, "setZustand(bool)", 1)

IMPLEMENT_OP_CALL(System_Tuer_setZustand_bool, Tuer, setZustand(p_Zustand), NO_OP())
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Tuer.cpp
*********************************************************************/
