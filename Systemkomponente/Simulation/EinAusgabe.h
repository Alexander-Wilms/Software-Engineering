/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: EinAusgabe
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/EinAusgabe.h
*********************************************************************/

#ifndef EinAusgabe_H
#define EinAusgabe_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## class EinAusgabe
#include "Station.h"
//## auto_generated
class Karussell;

//## auto_generated
class Kolben;

//## auto_generated
class Waage;

//## package System

//## class EinAusgabe
class EinAusgabe : public Station {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedEinAusgabe;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation EinAusgabe()
    EinAusgabe(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~EinAusgabe();
    
    ////    Operations    ////
    
    //## operation isOk()
    bool isOk();
    
    //## operation setGlas()
    void setGlas();
    
    ////    Additional operations    ////
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    ////    Framework operations    ////

public :

    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    //## statechart_method
    void Betrieb_entDef();
    
    //## statechart_method
    void Betrieb_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Betrieb_processEvent();
    
    //## statechart_method
    void state_5_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_5_processEvent();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Offen_handleEvent();
    
    //## statechart_method
    void state_4_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_processEvent();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Running_handleEvent();
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedEinAusgabe : public OMAnimatedStation {
    DECLARE_REACTIVE_META(EinAusgabe, OMAnimatedEinAusgabe)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Betrieb_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_5_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Zu_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Offen_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void state_4_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Stopped_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Running_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Idle_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/EinAusgabe.h
*********************************************************************/
