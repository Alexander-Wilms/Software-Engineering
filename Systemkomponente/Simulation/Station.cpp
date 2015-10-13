/********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Station
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Station.cpp
*********************************************************************/

//#[ ignore
#define NAMESPACE_PREFIX

#define _OMSTATECHART_ANIMATED
//#]

//## auto_generated
#include "Station.h"
//## link itsKarussell
#include "Karussell.h"
//## link itsKolben
#include "Kolben.h"
//## link itsWaage
#include "Waage.h"
//#[ ignore
#define System_Station_Station_SERIALIZE OM_NO_OP

#define System_Station_checkGlas_SERIALIZE OM_NO_OP

#define System_Station_clearBrutto_SERIALIZE OM_NO_OP

#define System_Station_dosiere_SERIALIZE aomsmethod->addAttribute("aMenge", x2String(aMenge));

#define System_Station_evReady_SERIALIZE OM_NO_OP

#define System_Station_fuellen_SERIALIZE OM_NO_OP

#define System_Station_getBrutto_SERIALIZE OM_NO_OP

#define System_Station_getGlas_SERIALIZE OM_NO_OP

#define System_Station_getNetto_SERIALIZE OM_NO_OP

#define System_Station_isOk_SERIALIZE OM_NO_OP

#define System_Station_setTara_SERIALIZE OM_NO_OP
//#]

//## package System

//## class Station
Station::Station(IOxfActive* theActiveContext) : MaxTime(10000) {
    NOTIFY_REACTIVE_CONSTRUCTOR(Station, Station(), 0, System_Station_Station_SERIALIZE);
    setActiveContext(theActiveContext, false);
    itsKarussell = NULL;
    {
        for (int pos = 0; pos < 2; ++pos) {
        	itsKolben[pos] = NULL;
        }
    }
    itsWaage = NULL;
    initStatechart();
}

Station::~Station() {
    NOTIFY_DESTRUCTOR(~Station, true);
    cleanUpRelations();
    cancelTimeouts();
}

bool Station::checkGlas() {
    NOTIFY_OPERATION(checkGlas, checkGlas(), 0, System_Station_checkGlas_SERIALIZE);
    //#[ operation checkGlas()
    return getBrutto() >= GlasGewicht;
    //#]
}

void Station::clearBrutto() {
    NOTIFY_OPERATION(clearBrutto, clearBrutto(), 0, System_Station_clearBrutto_SERIALIZE);
    //#[ operation clearBrutto()
     itsKarussell->clearBrutto(StationsNr);
    //#]
}

void Station::dosiere(int aMenge) {
    NOTIFY_OPERATION(dosiere, dosiere(int), 1, System_Station_dosiere_SERIALIZE);
    //#[ operation dosiere(int)
    itsKarussell->addWaage(StationsNr, aMenge);
    //#]
}

void Station::fuellen() {
    NOTIFY_OPERATION(fuellen, fuellen(), 0, System_Station_fuellen_SERIALIZE);
    //#[ operation fuellen()
    //#]
}

int Station::getBrutto() {
    NOTIFY_OPERATION(getBrutto, getBrutto(), 0, System_Station_getBrutto_SERIALIZE);
    //#[ operation getBrutto()
    return itsKarussell->getBrutto(StationsNr);
    //#]
}

void Station::getGlas() {
    NOTIFY_OPERATION(getGlas, getGlas(), 0, System_Station_getGlas_SERIALIZE);
    //#[ operation getGlas()
    // Glas rausnehmen
    	if ( getBrutto() > GlasGewicht ) {
    		clearBrutto();
    		itsKarussell->updateLED();
    		}
    //#]
}

int Station::getNetto() {
    NOTIFY_OPERATION(getNetto, getNetto(), 0, System_Station_getNetto_SERIALIZE);
    //#[ operation getNetto()
    return itsKarussell->getNetto(StationsNr);
    //#]
}

bool Station::isOk() {
    NOTIFY_OPERATION(isOk, isOk(), 0, System_Station_isOk_SERIALIZE);
    //#[ operation isOk()
    return Idle_IN() && Zu_IN();
    //#]
}

void Station::setTara() {
    NOTIFY_OPERATION(setTara, setTara(), 0, System_Station_setTara_SERIALIZE);
    //#[ operation setTara()
    itsKarussell->setTara(StationsNr);
    //#]
}

int Station::getDosierMenge() const {
    return DosierMenge;
}

void Station::setDosierMenge(int p_DosierMenge) {
    DosierMenge = p_DosierMenge;
}

bool Station::getError() const {
    return Error;
}

void Station::setError(bool p_Error) {
    Error = p_Error;
    NOTIFY_SET_OPERATION;
}

int Station::getMaxTime() const {
    return MaxTime;
}

void Station::setMaxTime(int p_MaxTime) {
    MaxTime = p_MaxTime;
}

int Station::getStationsNr() const {
    return StationsNr;
}

void Station::setStationsNr(int p_StationsNr) {
    StationsNr = p_StationsNr;
}

Karussell* Station::getItsKarussell() const {
    return itsKarussell;
}

void Station::setItsKarussell(Karussell* p_Karussell) {
    if(p_Karussell != NULL)
        {
            p_Karussell->_addItsStation(this);
        }
    _setItsKarussell(p_Karussell);
}

int Station::getItsKolben() const {
    int iter = 0;
    return iter;
}

void Station::addItsKolben(Kolben* p_Kolben) {
    if(p_Kolben != NULL)
        {
            p_Kolben->_setItsStation(this);
        }
    _addItsKolben(p_Kolben);
}

void Station::removeItsKolben(Kolben* p_Kolben) {
    if(p_Kolben != NULL)
        {
            p_Kolben->__setItsStation(NULL);
        }
    _removeItsKolben(p_Kolben);
}

void Station::clearItsKolben() {
    int iter = 0;
    while ((iter < 2) && itsKolben[iter]){
        (itsKolben[iter])->_clearItsStation();
        iter++;
    }
    _clearItsKolben();
}

Tuer* Station::getItsTuer() const {
    return (Tuer*) &itsTuer;
}

Waage* Station::getItsWaage() const {
    return itsWaage;
}

void Station::setItsWaage(Waage* p_Waage) {
    itsWaage = p_Waage;
    if(p_Waage != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsWaage", p_Waage, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsWaage");
        }
}

bool Station::startBehavior() {
    bool done = true;
    done &= OMReactive::startBehavior();
    return done;
}

void Station::initStatechart() {
    rootState_subState = OMNonState;
    rootState_active = OMNonState;
    state_5_subState = OMNonState;
    state_5_active = OMNonState;
    state_5_timeout = NULL;
    state_4_subState = OMNonState;
    state_4_active = OMNonState;
    state_4_timeout = NULL;
}

void Station::cleanUpRelations() {
    if(itsKarussell != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsKarussell");
            Karussell* current = itsKarussell;
            if(current != NULL)
                {
                    current->_removeItsStation(this);
                }
            itsKarussell = NULL;
        }
    {
        int iter = 0;
        while ((iter < 2) && itsKolben[iter]){
            Station* p_Station = (itsKolben[iter])->getItsStation();
            if(p_Station != NULL)
                {
                    (itsKolben[iter])->__setItsStation(NULL);
                }
            iter++;
        }
    }
    if(itsWaage != NULL)
        {
            NOTIFY_RELATION_CLEARED("itsWaage");
            itsWaage = NULL;
        }
}

void Station::cancelTimeouts() {
    cancel(state_5_timeout);
    cancel(state_4_timeout);
}

bool Station::cancelTimeout(const IOxfTimeout* arg) {
    bool res = false;
    if(state_5_timeout == arg)
        {
            state_5_timeout = NULL;
            res = true;
        }
    if(state_4_timeout == arg)
        {
            state_4_timeout = NULL;
            res = true;
        }
    return res;
}

//#[ ignore
#undef OM_RET_TYPE
#define OM_RET_TYPE 
#undef OM_SER_RET
#define OM_SER_RET(val) 
#undef OM_SER_OUT
#define OM_SER_OUT 
//#]


void Station::evReady() {
    NOTIFY_TRIGGERED_OPERATION(evReady, evReady(), 0, System_Station_evReady_SERIALIZE);
    evReady_Station_Event triggerEvent;
    handleTrigger(&triggerEvent);
    OM_RETURN_VOID;
}

void Station::__setItsKarussell(Karussell* p_Karussell) {
    itsKarussell = p_Karussell;
    if(p_Karussell != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsKarussell", p_Karussell, false, true);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsKarussell");
        }
}

void Station::_setItsKarussell(Karussell* p_Karussell) {
    if(itsKarussell != NULL)
        {
            itsKarussell->_removeItsStation(this);
        }
    __setItsKarussell(p_Karussell);
}

void Station::_clearItsKarussell() {
    NOTIFY_RELATION_CLEARED("itsKarussell");
    itsKarussell = NULL;
}

void Station::_addItsKolben(Kolben* p_Kolben) {
    if(p_Kolben != NULL)
        {
            NOTIFY_RELATION_ITEM_ADDED("itsKolben", p_Kolben, false, false);
        }
    else
        {
            NOTIFY_RELATION_CLEARED("itsKolben");
        }
    for (int pos = 0; pos < 2; ++pos) {
    	if (!itsKolben[pos]) {
    		itsKolben[pos] = p_Kolben;
    		break;
    	}
    }
}

void Station::_removeItsKolben(Kolben* p_Kolben) {
    NOTIFY_RELATION_ITEM_REMOVED("itsKolben", p_Kolben);
    for (int pos = 0; pos < 2; ++pos) {
    	if (itsKolben[pos] == p_Kolben) {
    		itsKolben[pos] = NULL;
    	}
    }
}

void Station::_clearItsKolben() {
    NOTIFY_RELATION_CLEARED("itsKolben");
    
}

void Station::rootState_entDef() {
    {
        NOTIFY_STATE_ENTERED("ROOT");
        NOTIFY_TRANSITION_STARTED("9");
        Betrieb_entDef();
        NOTIFY_TRANSITION_TERMINATED("9");
    }
}

IOxfReactive::TakeEventStatus Station::rootState_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State Betrieb
    if(rootState_active == Betrieb)
        {
            res = Betrieb_processEvent();
        }
    return res;
}

void Station::Betrieb_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb");
    rootState_subState = Betrieb;
    rootState_active = Betrieb;
    state_4_entDef();
    state_5_entDef();
}

void Station::Betrieb_exit() {
    switch (state_4_subState) {
        // State Idle
        case Idle:
        {
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle");
        }
        break;
        // State Running
        case Running:
        {
            popNullTransition();
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
        }
        break;
        // State Stopped
        case Stopped:
        {
            //#[ state Betrieb.state_4.Stopped.(Exit) 
            Error = false;
            //#]
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Stopped");
        }
        break;
        default:
            break;
    }
    state_4_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4");
    switch (state_5_subState) {
        // State Offen
        case Offen:
        {
            popNullTransition();
            cancel(state_5_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Offen");
        }
        break;
        // State Zu
        case Zu:
        {
            popNullTransition();
            cancel(state_5_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Zu");
        }
        break;
        default:
            break;
    }
    state_5_subState = OMNonState;
    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5");
    
    NOTIFY_STATE_EXITED("ROOT.Betrieb");
}

IOxfReactive::TakeEventStatus Station::Betrieb_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    // State state_4
    if(state_4_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Betrieb))
                {
                    return res;
                }
        }
    // State state_5
    if(state_5_processEvent() != eventNotConsumed)
        {
            res = eventConsumed;
            if(!IS_IN(Betrieb))
                {
                    return res;
                }
        }
    
    return res;
}

void Station::state_5_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5");
    NOTIFY_TRANSITION_STARTED("10");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
    pushNullTransition();
    state_5_subState = Offen;
    state_5_active = Offen;
    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
    NOTIFY_TRANSITION_TERMINATED("10");
}

IOxfReactive::TakeEventStatus Station::state_5_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_5_active) {
        // State Offen
        case Offen:
        {
            res = Offen_handleEvent();
        }
        break;
        // State Zu
        case Zu:
        {
            if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
                {
                    if(getCurrentEvent() == state_5_timeout)
                        {
                            NOTIFY_TRANSITION_STARTED("6");
                            popNullTransition();
                            cancel(state_5_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Zu");
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Zu");
                            pushNullTransition();
                            state_5_subState = Zu;
                            state_5_active = Zu;
                            state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Zu");
                            NOTIFY_TRANSITION_TERMINATED("6");
                            res = eventConsumed;
                        }
                }
            else if(IS_EVENT_TYPE_OF(OMNullEventId))
                {
                    //## transition 8 
                    if(!itsTuer.getZustand())
                        {
                            NOTIFY_TRANSITION_STARTED("8");
                            popNullTransition();
                            cancel(state_5_timeout);
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Zu");
                            //#[ transition 8 
                            GEN(evStop);
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
                            pushNullTransition();
                            state_5_subState = Offen;
                            state_5_active = Offen;
                            state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
                            NOTIFY_TRANSITION_TERMINATED("8");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

IOxfReactive::TakeEventStatus Station::Offen_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evFuellen_System_id))
        {
            NOTIFY_TRANSITION_STARTED("12");
            //#[ transition 12 
            fuellen();
            //#]
            NOTIFY_TRANSITION_TERMINATED("12");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(evNoGlas_System_id))
        {
            NOTIFY_TRANSITION_STARTED("11");
            //#[ transition 11 
            getGlas();
            //#]
            NOTIFY_TRANSITION_TERMINATED("11");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_5_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("5");
                    popNullTransition();
                    cancel(state_5_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Offen");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Offen");
                    pushNullTransition();
                    state_5_subState = Offen;
                    state_5_active = Offen;
                    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Offen");
                    NOTIFY_TRANSITION_TERMINATED("5");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            //## transition 7 
            if(itsTuer.getZustand())
                {
                    NOTIFY_TRANSITION_STARTED("7");
                    popNullTransition();
                    cancel(state_5_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_5.Offen");
                    //#[ transition 7 
                     GEN(evContinue);
                    //#]
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_5.Zu");
                    pushNullTransition();
                    state_5_subState = Zu;
                    state_5_active = Zu;
                    state_5_timeout = scheduleTimeout(500, "ROOT.Betrieb.state_5.Zu");
                    NOTIFY_TRANSITION_TERMINATED("7");
                    res = eventConsumed;
                }
        }
    
    
    return res;
}

void Station::state_4_entDef() {
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4");
    NOTIFY_TRANSITION_STARTED("0");
    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
    state_4_subState = Idle;
    state_4_active = Idle;
    NOTIFY_TRANSITION_TERMINATED("0");
}

IOxfReactive::TakeEventStatus Station::state_4_processEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    switch (state_4_active) {
        // State Idle
        case Idle:
        {
            if(IS_EVENT_TYPE_OF(evRun_System_id))
                {
                    //## transition 1 
                    if(checkGlas())
                        {
                            NOTIFY_TRANSITION_STARTED("1");
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Idle");
                            //#[ transition 1 
                            setTara();
                            //#]
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
                            pushNullTransition();
                            state_4_subState = Running;
                            state_4_active = Running;
                            state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
                            NOTIFY_TRANSITION_TERMINATED("1");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        // State Running
        case Running:
        {
            res = Running_handleEvent();
        }
        break;
        // State Stopped
        case Stopped:
        {
            if(IS_EVENT_TYPE_OF(evContinue_System_id))
                {
                    //## transition 15 
                    if(checkGlas())
                        {
                            NOTIFY_TRANSITION_STARTED("3");
                            NOTIFY_TRANSITION_STARTED("15");
                            //#[ state Betrieb.state_4.Stopped.(Exit) 
                            Error = false;
                            //#]
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Stopped");
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Running");
                            pushNullTransition();
                            state_4_subState = Running;
                            state_4_active = Running;
                            state_4_timeout = scheduleTimeout(MaxTime, "ROOT.Betrieb.state_4.Running");
                            NOTIFY_TRANSITION_TERMINATED("15");
                            NOTIFY_TRANSITION_TERMINATED("3");
                            res = eventConsumed;
                        }
                    else
                        {
                            NOTIFY_TRANSITION_STARTED("3");
                            NOTIFY_TRANSITION_STARTED("14");
                            //#[ state Betrieb.state_4.Stopped.(Exit) 
                            Error = false;
                            //#]
                            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Stopped");
                            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
                            state_4_subState = Idle;
                            state_4_active = Idle;
                            NOTIFY_TRANSITION_TERMINATED("14");
                            NOTIFY_TRANSITION_TERMINATED("3");
                            res = eventConsumed;
                        }
                }
            
            
        }
        break;
        default:
            break;
    }
    return res;
}

IOxfReactive::TakeEventStatus Station::Running_handleEvent() {
    IOxfReactive::TakeEventStatus res = eventNotConsumed;
    if(IS_EVENT_TYPE_OF(evStop_System_id))
        {
            NOTIFY_TRANSITION_STARTED("2");
            popNullTransition();
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Stopped");
            state_4_subState = Stopped;
            state_4_active = Stopped;
            //#[ state Betrieb.state_4.Stopped.(Entry) 
            Error = true;
            //#]
            NOTIFY_TRANSITION_TERMINATED("2");
            res = eventConsumed;
        }
    else if(IS_EVENT_TYPE_OF(OMTimeoutEventId))
        {
            if(getCurrentEvent() == state_4_timeout)
                {
                    NOTIFY_TRANSITION_STARTED("13");
                    popNullTransition();
                    cancel(state_4_timeout);
                    NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
                    NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Stopped");
                    state_4_subState = Stopped;
                    state_4_active = Stopped;
                    //#[ state Betrieb.state_4.Stopped.(Entry) 
                    Error = true;
                    //#]
                    NOTIFY_TRANSITION_TERMINATED("13");
                    res = eventConsumed;
                }
        }
    else if(IS_EVENT_TYPE_OF(OMNullEventId))
        {
            NOTIFY_TRANSITION_STARTED("4");
            popNullTransition();
            cancel(state_4_timeout);
            NOTIFY_STATE_EXITED("ROOT.Betrieb.state_4.Running");
            NOTIFY_STATE_ENTERED("ROOT.Betrieb.state_4.Idle");
            state_4_subState = Idle;
            state_4_active = Idle;
            NOTIFY_TRANSITION_TERMINATED("4");
            res = eventConsumed;
        }
    
    
    return res;
}

#ifdef _OMINSTRUMENT
//#[ ignore
void OMAnimatedStation::serializeAttributes(AOMSAttributes* aomsAttributes) const {
    aomsAttributes->addAttribute("StationsNr", x2String(myReal->StationsNr));
    aomsAttributes->addAttribute("Error", x2String(myReal->Error));
    aomsAttributes->addAttribute("DosierMenge", x2String(myReal->DosierMenge));
    aomsAttributes->addAttribute("MaxTime", x2String(myReal->MaxTime));
}

void OMAnimatedStation::serializeRelations(AOMSRelations* aomsRelations) const {
    aomsRelations->addRelation("itsTuer", true, true);
    aomsRelations->ADD_ITEM(&myReal->itsTuer);
    aomsRelations->addRelation("itsKarussell", false, true);
    if(myReal->itsKarussell)
        {
            aomsRelations->ADD_ITEM(myReal->itsKarussell);
        }
    aomsRelations->addRelation("itsWaage", false, true);
    if(myReal->itsWaage)
        {
            aomsRelations->ADD_ITEM(myReal->itsWaage);
        }
    aomsRelations->addRelation("itsKolben", false, false);
    {
        int iter = 0;
        while ((iter < 2) && myReal->itsKolben[iter]){
            aomsRelations->ADD_ITEM(myReal->itsKolben[iter]);
            iter++;
        }
    }
}

void OMAnimatedStation::rootState_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT");
    if(myReal->rootState_subState == Station::Betrieb)
        {
            Betrieb_serializeStates(aomsState);
        }
}

void OMAnimatedStation::Betrieb_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb");
    state_4_serializeStates(aomsState);
    state_5_serializeStates(aomsState);
}

void OMAnimatedStation::state_5_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5");
    switch (myReal->state_5_subState) {
        case Station::Offen:
        {
            Offen_serializeStates(aomsState);
        }
        break;
        case Station::Zu:
        {
            Zu_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedStation::Zu_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Zu");
}

void OMAnimatedStation::Offen_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_5.Offen");
}

void OMAnimatedStation::state_4_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4");
    switch (myReal->state_4_subState) {
        case Station::Idle:
        {
            Idle_serializeStates(aomsState);
        }
        break;
        case Station::Running:
        {
            Running_serializeStates(aomsState);
        }
        break;
        case Station::Stopped:
        {
            Stopped_serializeStates(aomsState);
        }
        break;
        default:
            break;
    }
}

void OMAnimatedStation::Stopped_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Stopped");
}

void OMAnimatedStation::Running_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Running");
}

void OMAnimatedStation::Idle_serializeStates(AOMSState* aomsState) const {
    aomsState->addState("ROOT.Betrieb.state_4.Idle");
}
//#]

IMPLEMENT_REACTIVE_META_P(Station, System, System, false, OMAnimatedStation)
#endif // _OMINSTRUMENT

//#[ ignore
evReady_Station_Event::evReady_Station_Event() {
    setId(evReady_Station_Event_id);
}
//#]

/*********************************************************************
	File Path	: Systemkomponente/Simulation/Station.cpp
*********************************************************************/
