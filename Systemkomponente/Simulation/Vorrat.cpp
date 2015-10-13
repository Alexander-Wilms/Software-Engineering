/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Vorrat
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Vorrat.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Vorrat.h"
//#[ ignore
#define System_Vorrat_Vorrat_SERIALIZE OM_NO_OP

#define System_Vorrat_entnehme_SERIALIZE aomsmethod->addAttribute("aMenge", x2String(aMenge));

#define System_Vorrat_fuelle_SERIALIZE OM_NO_OP

#define System_Vorrat_getVorrat_SERIALIZE OM_NO_OP

#define System_Vorrat_setMaxVorrat_SERIALIZE aomsmethod->addAttribute("input", x2String(input));

#define System_Vorrat_setVorhandenerVorrat_SERIALIZE aomsmethod->addAttribute("input", x2String(input));
//#]

//## package System

//## class Vorrat
Vorrat::Vorrat() : MaxVorrat(100), VorhandenerVorrat(100) {
    NOTIFY_CONSTRUCTOR(Vorrat, Vorrat(), 0, System_Vorrat_Vorrat_SERIALIZE);
}

Vorrat::~Vorrat() {
    NOTIFY_DESTRUCTOR(~Vorrat, true);
}

int Vorrat::entnehme(int aMenge) {
    NOTIFY_OPERATION(entnehme, entnehme(int), 1, System_Vorrat_entnehme_SERIALIZE);
    //#[ operation entnehme(int)
    // Vorrat nicht < 0
    if( VorhandenerVorrat <= aMenge ) {
    	aMenge = VorhandenerVorrat;
    }
    VorhandenerVorrat -= aMenge;
    return aMenge;
    
    	  
    //#]
}

void Vorrat::fuelle() {
    NOTIFY_OPERATION(fuelle, fuelle(), 0, System_Vorrat_fuelle_SERIALIZE);
    //#[ operation fuelle()
    // Nur Nachfüllen, wenn Tür von Station Zucker auf ist
    //if(Zucker.itsTuer.getZustand() == true)
    //{
    	VorhandenerVorrat = MaxVorrat;
    //}
    //#]
}

int Vorrat::getVorrat() {
    NOTIFY_OPERATION(getVorrat, getVorrat(), 0, System_Vorrat_getVorrat_SERIALIZE);
    //#[ operation getVorrat()
    return VorhandenerVorrat;
    //#]
}

void Vorrat::setMaxVorrat(int input) {
    NOTIFY_OPERATION(setMaxVorrat, setMaxVorrat(int), 1, System_Vorrat_setMaxVorrat_SERIALIZE);
    //#[ operation setMaxVorrat(int)
    MaxVorrat = input;
    //#]
}

void Vorrat::setVorhandenerVorrat(int input) {
    NOTIFY_OPERATION(setVorhandenerVorrat, setVorhandenerVorrat(int), 1, System_Vorrat_setVorhandenerVorrat_SERIALIZE);
    //#[ operation setVorhandenerVorrat(int)
    VorhandenerVorrat = input;
    //#]
    NOTIFY_SET_OPERATION;
}

int Vorrat::getMaxVorrat() const {
    return MaxVorrat;
}

int Vorrat::getVorhandenerVorrat() const {
    return VorhandenerVorrat;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedVorrat::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("VorhandenerVorrat", x2String(myReal->VorhandenerVorrat));
    aomsAttributes->addAttribute("MaxVorrat", x2String(myReal->MaxVorrat));
}
//#]

IMPLEMENT_META_P(Vorrat, System, System, false, OMAnimatedVorrat)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Vorrat.cpp
*********************************************************************/
