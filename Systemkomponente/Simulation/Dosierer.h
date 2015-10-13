/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Dosierer
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Dosierer.h
*********************************************************************/

#ifndef Dosierer_H
#define Dosierer_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## auto_generated
#include <oxf/omthread.h>
//## auto_generated
#include <oxf/omreactive.h>
//## auto_generated
#include <oxf/state.h>
//## auto_generated
#include <oxf/event.h>
//## link itsStation
class Station;

//## link itsVorrat
class Vorrat;

//## package System

//## class Dosierer
class Dosierer : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedDosierer;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Dosierer(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Dosierer();
    
    ////    Operations    ////
    
    //## operation dosiere()
    void dosiere();
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getDosierMenge() const;
    
    //## auto_generated
    void setDosierMenge(int p_DosierMenge);
    
    //## auto_generated
    int getRunde() const;
    
    //## auto_generated
    void setRunde(int p_runde);
    
    //## auto_generated
    Station* getItsStation() const;
    
    //## auto_generated
    void setItsStation(Station* p_Station);
    
    //## auto_generated
    Vorrat* getItsVorrat() const;
    
    //## auto_generated
    void setItsVorrat(Vorrat* p_Vorrat);
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initStatechart();
    
    //## auto_generated
    void cleanUpRelations();
    
    //## auto_generated
    void cancelTimeouts();
    
    //## auto_generated
    bool cancelTimeout(const IOxfTimeout* arg);
    
    ////    Attributes    ////
    
    int DosierMenge;		//## attribute DosierMenge
    
    int runde;		//## attribute runde
    
    ////    Relations and components    ////
    
    Station* itsStation;		//## link itsStation
    
    Vorrat* itsVorrat;		//## link itsVorrat
    
    ////    Framework operations    ////
    
    ////    Framework    ////

public :

    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // Running:
    //## statechart_method
    inline bool Running_IN() const;
    
    // Idle:
    //## statechart_method
    inline bool Idle_IN() const;

protected :

//#[ ignore
    enum Dosierer_Enum {
        OMNonState = 0,
        Running = 1,
        Idle = 2
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    IOxfTimeout* rootState_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedDosierer : virtual public AOMInstance {
    DECLARE_REACTIVE_META(Dosierer, OMAnimatedDosierer)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Running_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void Idle_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Dosierer::rootState_IN() const {
    return true;
}

inline bool Dosierer::Running_IN() const {
    return rootState_subState == Running;
}

inline bool Dosierer::Idle_IN() const {
    return rootState_subState == Idle;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Dosierer.h
*********************************************************************/
