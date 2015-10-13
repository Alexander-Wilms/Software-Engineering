/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: System
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/System.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX
//#]

//## auto_generated
#include "System.h"
//## classInstance CaipiAutomat
#include "Caipisystem.h"
//## auto_generated
#include "Abfuellstation.h"
//## auto_generated
#include "Cachacca.h"
//## auto_generated
#include "Dosierer.h"
//## auto_generated
#include "EinAusgabe.h"
//## auto_generated
#include "Eis.h"
//## auto_generated
#include "Karussell.h"
//## auto_generated
#include "Kolben.h"
//## auto_generated
#include "Led.h"
//## auto_generated
#include "Lichtschranke.h"
//## auto_generated
#include "Limetten.h"
//## auto_generated
#include "Limettenschneider.h"
//## auto_generated
#include "Stampfer.h"
//## auto_generated
#include "Station.h"
//## auto_generated
#include "Tuer.h"
//## auto_generated
#include "Vorrat.h"
//## auto_generated
#include "Waage.h"
//## auto_generated
#include "Zucker.h"
//#[ ignore
#define evGlas_SERIALIZE OM_NO_OP

#define evGlas_UNSERIALIZE OM_NO_OP

#define evGlas_CONSTRUCTOR evGlas()

#define evNoGlas_SERIALIZE OM_NO_OP

#define evNoGlas_UNSERIALIZE OM_NO_OP

#define evNoGlas_CONSTRUCTOR evNoGlas()

#define evRun_SERIALIZE OM_NO_OP

#define evRun_UNSERIALIZE OM_NO_OP

#define evRun_CONSTRUCTOR evRun()

#define evStop_SERIALIZE OM_NO_OP

#define evStop_UNSERIALIZE OM_NO_OP

#define evStop_CONSTRUCTOR evStop()

#define evContinue_SERIALIZE OM_NO_OP

#define evContinue_UNSERIALIZE OM_NO_OP

#define evContinue_CONSTRUCTOR evContinue()

#define evFuellen_SERIALIZE OM_NO_OP

#define evFuellen_UNSERIALIZE OM_NO_OP

#define evFuellen_CONSTRUCTOR evFuellen()

#define moveup_SERIALIZE OM_NO_OP

#define moveup_UNSERIALIZE OM_NO_OP

#define moveup_CONSTRUCTOR moveup()

#define movedown_SERIALIZE OM_NO_OP

#define movedown_UNSERIALIZE OM_NO_OP

#define movedown_CONSTRUCTOR movedown()

#define evNoLimette_SERIALIZE OM_NO_OP

#define evNoLimette_UNSERIALIZE OM_NO_OP

#define evNoLimette_CONSTRUCTOR evNoLimette()

#define evSReady_SERIALIZE OM_NO_OP

#define evSReady_UNSERIALIZE OM_NO_OP

#define evSReady_CONSTRUCTOR evSReady()

#define evReady_SERIALIZE OM_NO_OP

#define evReady_UNSERIALIZE OM_NO_OP

#define evReady_CONSTRUCTOR evReady()

#define evLIMReady_SERIALIZE OM_NO_OP

#define evLIMReady_UNSERIALIZE OM_NO_OP

#define evLIMReady_CONSTRUCTOR evLIMReady()
//#]

//## package System


#ifdef _OMINSTRUMENT
static void serializeGlobalVars(AOMSAttributes* aomsAttributes);

static void RenameGlobalInstances();

IMPLEMENT_META_PACKAGE(System, System)

static void serializeGlobalVars(AOMSAttributes* aomsAttributes) {
    aomsAttributes->addAttribute("MaxStation", x2String(MaxStation));
    aomsAttributes->addAttribute("GlasGewicht", x2String(GlasGewicht));
}

static void RenameGlobalInstances() {
    OM_SET_INSTANCE_NAME(&CaipiAutomat, Caipisystem, "CaipiAutomat", AOMNoMultiplicity);
}
#endif // _OMINSTRUMENT

//## classInstance CaipiAutomat
Caipisystem CaipiAutomat;

void System_initRelations() {
    {
        {
            CaipiAutomat.setShouldDelete(false);
        }
    }
    
    #ifdef _OMINSTRUMENT
    RenameGlobalInstances();
    #endif // _OMINSTRUMENT
}

bool System_startBehavior() {
    bool done = true;
    done &= CaipiAutomat.startBehavior();
    return done;
}

//#[ ignore
System_OMInitializer::System_OMInitializer() {
    System_initRelations();
    System_startBehavior();
}

System_OMInitializer::~System_OMInitializer() {
}
//#]

//## event evGlas()
evGlas::evGlas() {
    NOTIFY_EVENT_CONSTRUCTOR(evGlas)
    setId(evGlas_System_id);
}

bool evGlas::isTypeOf(const short id) const {
    return (evGlas_System_id==id);
}

IMPLEMENT_META_EVENT_P(evGlas, System, System, evGlas())

//## event evNoGlas()
evNoGlas::evNoGlas() {
    NOTIFY_EVENT_CONSTRUCTOR(evNoGlas)
    setId(evNoGlas_System_id);
}

bool evNoGlas::isTypeOf(const short id) const {
    return (evNoGlas_System_id==id);
}

IMPLEMENT_META_EVENT_P(evNoGlas, System, System, evNoGlas())

//## event evRun()
evRun::evRun() {
    NOTIFY_EVENT_CONSTRUCTOR(evRun)
    setId(evRun_System_id);
}

bool evRun::isTypeOf(const short id) const {
    return (evRun_System_id==id);
}

IMPLEMENT_META_EVENT_P(evRun, System, System, evRun())

//## event evStop()
evStop::evStop() {
    NOTIFY_EVENT_CONSTRUCTOR(evStop)
    setId(evStop_System_id);
}

bool evStop::isTypeOf(const short id) const {
    return (evStop_System_id==id);
}

IMPLEMENT_META_EVENT_P(evStop, System, System, evStop())

//## event evContinue()
evContinue::evContinue() {
    NOTIFY_EVENT_CONSTRUCTOR(evContinue)
    setId(evContinue_System_id);
}

bool evContinue::isTypeOf(const short id) const {
    return (evContinue_System_id==id);
}

IMPLEMENT_META_EVENT_P(evContinue, System, System, evContinue())

//## event evFuellen()
evFuellen::evFuellen() {
    NOTIFY_EVENT_CONSTRUCTOR(evFuellen)
    setId(evFuellen_System_id);
}

bool evFuellen::isTypeOf(const short id) const {
    return (evFuellen_System_id==id);
}

IMPLEMENT_META_EVENT_P(evFuellen, System, System, evFuellen())

//## event moveup()
moveup::moveup() {
    NOTIFY_EVENT_CONSTRUCTOR(moveup)
    setId(moveup_System_id);
}

bool moveup::isTypeOf(const short id) const {
    return (moveup_System_id==id);
}

IMPLEMENT_META_EVENT_P(moveup, System, System, moveup())

//## event movedown()
movedown::movedown() {
    NOTIFY_EVENT_CONSTRUCTOR(movedown)
    setId(movedown_System_id);
}

bool movedown::isTypeOf(const short id) const {
    return (movedown_System_id==id);
}

IMPLEMENT_META_EVENT_P(movedown, System, System, movedown())

//## event evNoLimette()
evNoLimette::evNoLimette() {
    NOTIFY_EVENT_CONSTRUCTOR(evNoLimette)
    setId(evNoLimette_System_id);
}

bool evNoLimette::isTypeOf(const short id) const {
    return (evNoLimette_System_id==id);
}

IMPLEMENT_META_EVENT_P(evNoLimette, System, System, evNoLimette())

//## event evSReady()
evSReady::evSReady() {
    NOTIFY_EVENT_CONSTRUCTOR(evSReady)
    setId(evSReady_System_id);
}

bool evSReady::isTypeOf(const short id) const {
    return (evSReady_System_id==id);
}

IMPLEMENT_META_EVENT_P(evSReady, System, System, evSReady())

//## event evReady()
evReady::evReady() {
    NOTIFY_EVENT_CONSTRUCTOR(evReady)
    setId(evReady_System_id);
}

bool evReady::isTypeOf(const short id) const {
    return (evReady_System_id==id);
}

IMPLEMENT_META_EVENT_P(evReady, System, System, evReady())

//## event evLIMReady()
evLIMReady::evLIMReady() {
    NOTIFY_EVENT_CONSTRUCTOR(evLIMReady)
    setId(evLIMReady_System_id);
}

bool evLIMReady::isTypeOf(const short id) const {
    return (evLIMReady_System_id==id);
}

IMPLEMENT_META_EVENT_P(evLIMReady, System, System, evLIMReady())

/*********************************************************************
	File Path	: Systemkomponente/Simulation/System.cpp
*********************************************************************/
