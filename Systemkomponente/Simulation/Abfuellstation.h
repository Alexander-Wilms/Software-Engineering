/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Abfuellstation
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Abfuellstation.h
*********************************************************************/

#ifndef Abfuellstation_H
#define Abfuellstation_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## classInstance itsDosierer
#include "Dosierer.h"
//## class Abfuellstation
#include "Station.h"
//## classInstance itsVorrat
#include "Vorrat.h"
//## auto_generated
class Karussell;

//## auto_generated
class Kolben;

//## auto_generated
class Waage;

//## package System

//## class Abfuellstation
class Abfuellstation : public Station {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedAbfuellstation;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation Abfuellstation()
    Abfuellstation(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Abfuellstation();
    
    ////    Operations    ////
    
    //## operation fuellen()
    void fuellen();
    
    //## operation getitsVorrat()
    Vorrat* getitsVorrat();
    
    ////    Additional operations    ////
    
    //## auto_generated
    Dosierer* getItsDosierer() const;
    
    //## auto_generated
    Vorrat* getItsVorrat() const;
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initRelations();
    
    //## auto_generated
    void initStatechart();
    
    ////    Relations and components    ////
    
    Dosierer itsDosierer;		//## classInstance itsDosierer
    
    Vorrat itsVorrat;		//## classInstance itsVorrat
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void setActiveContext(IOxfActive* theActiveContext, bool activeInstance);
    
    //## auto_generated
    virtual void destroy();
    
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
class OMAnimatedAbfuellstation : public OMAnimatedStation {
    DECLARE_REACTIVE_META(Abfuellstation, OMAnimatedAbfuellstation)
    
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
	File Path	: Systemkomponente/Simulation/Abfuellstation.h
*********************************************************************/
