/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Waage
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Waage.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Waage.h"
//#[ ignore
#define System_Waage_Waage_SERIALIZE OM_NO_OP

#define System_Waage_addBrutto_SERIALIZE aomsmethod->addAttribute("aGewicht", x2String(aGewicht));

#define System_Waage_clearBrutto_SERIALIZE OM_NO_OP

#define System_Waage_getNetto_SERIALIZE OM_NO_OP

#define System_Waage_setTara_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Waage
Waage::Waage() {
    NOTIFY_CONSTRUCTOR(Waage, Waage(), 0, System_Waage_Waage_SERIALIZE);
}

Waage::~Waage() {
    NOTIFY_DESTRUCTOR(~Waage, true);
}

void Waage::addBrutto(int aGewicht) {
    NOTIFY_OPERATION(addBrutto, addBrutto(int), 1, System_Waage_addBrutto_SERIALIZE);
    //#[ operation addBrutto(int)
    Brutto += aGewicht;
    //#]
}

void Waage::clearBrutto() {
    NOTIFY_OPERATION(clearBrutto, clearBrutto(), 0, System_Waage_clearBrutto_SERIALIZE);
    //#[ operation clearBrutto()
    Brutto = 0;
    //#]
}

int Waage::getNetto() {
    NOTIFY_OPERATION(getNetto, getNetto(), 0, System_Waage_getNetto_SERIALIZE);
    //#[ operation getNetto()
    return Brutto - Tara;
    //#]
}

void Waage::setTara() {
    NOTIFY_OPERATION(setTara, setTara(), 0, System_Waage_setTara_SERIALIZE);
    //#[ operation setTara()
    Tara = Brutto;
    //#]
}

int Waage::getBrutto() const {
    return Brutto;
}

void Waage::setBrutto(int p_Brutto) {
    Brutto = p_Brutto;
    NOTIFY_SET_OPERATION;
}

int Waage::getTara() const {
    return Tara;
}

void Waage::setTara(int p_Tara) {
    Tara = p_Tara;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedWaage::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("Brutto", x2String(myReal->Brutto));
    aomsAttributes->addAttribute("Tara", x2String(myReal->Tara));
}
//#]

IMPLEMENT_META_P(Waage, System, System, false, OMAnimatedWaage)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Waage.cpp
*********************************************************************/
