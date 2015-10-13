/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Lichtschranke
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Lichtschranke.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "Lichtschranke.h"
//## link itsLimetten
#include "Limetten.h"
//## link itsStation
#include "Station.h"
//#[ ignore
#define System_Lichtschranke_Lichtschranke_SERIALIZE OM_NO_OP

#define System_Lichtschranke_check_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Lichtschranke
Lichtschranke::Lichtschranke() {
    NOTIFY_CONSTRUCTOR(Lichtschranke, Lichtschranke(), 0, System_Lichtschranke_Lichtschranke_SERIALIZE);
    itsLimetten = NULL;
    itsStation = NULL;
}

Lichtschranke::~Lichtschranke() {
    NOTIFY_DESTRUCTOR(~Lichtschranke, true);
    cleanUpRelations();
}

bool Lichtschranke::check() {
    NOTIFY_OPERATION(check, check(), 0, System_Lichtschranke_check_SERIALIZE);
    //#[ operation check()
    if(itsLimetten->getitsVorrat()->getVorrat()>0)
    {
    	itsLimetten->getitsVorrat()->entnehme(1);
    	return true;
    } else {
    	return false;
    }
    //#]
}

Limetten* Lichtschranke::getItsLimetten() const {
    return itsLimetten;
}

void Lichtschranke::setItsLimetten(Limetten* p_Limetten) {
    itsLimetten = p_Limetten;
    if(p_Limetten != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsLimetten", p_Limetten, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsLimetten");
        }
}

Station* Lichtschranke::getItsStation() const {
    return itsStation;
}

void Lichtschranke::setItsStation(Station* p_Station) {
    itsStation = p_Station;
    if(p_Station != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsStation", p_Station, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsStation");
        }
}

void Lichtschranke::cleanUpRelations() {
    if(itsLimetten != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsLimetten");
            itsLimetten = NULL;
        }
    if(itsStation != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsStation");
            itsStation = NULL;
        }
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedLichtschranke::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsLimetten", false, true);
    if(myReal->itsLimetten)
        {
            aomsRelations->ADD_ITEM(myReal->itsLimetten);
        }
    aomsRelations->addRelation("itsStation", false, true);
    if(myReal->itsStation)
        {
            aomsRelations->ADD_ITEM(myReal->itsStation);
        }
}
//#]

IMPLEMENT_META_P(Lichtschranke, System, System, false, OMAnimatedLichtschranke)
#endif // _OMINSTRUMENT

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Lichtschranke.cpp
*********************************************************************/
