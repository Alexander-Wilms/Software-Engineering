/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Station
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Station.h
*********************************************************************/

#ifndef Station_H
#define Station_H

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
//## classInstance itsTuer
#include "Tuer.h"
//## link itsKarussell
class Karussell;

//## link itsKolben
class Kolben;

//## link itsWaage
class Waage;

//#[ ignore
#define evReady_Station_Event_id 31000
//#]

//## package System

//## class Station
class Station : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedStation;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Station(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    virtual ~Station();
    
    ////    Operations    ////
    
    //## operation checkGlas()
    bool checkGlas();
    
    //## operation clearBrutto()
    void clearBrutto();
    
    //## operation dosiere(int)
    void dosiere(int aMenge);
    
    //## operation fuellen()
    virtual void fuellen();
    
    //## operation getBrutto()
    int getBrutto();
    
    //## operation getGlas()
    void getGlas();
    
    //## operation getNetto()
    int getNetto();
    
    //## operation isOk()
    virtual bool isOk();
    
    //## operation setTara()
    void setTara();
    
    ////    Additional operations    ////
    
    //## auto_generated
    int getDosierMenge() const;
    
    //## auto_generated
    void setDosierMenge(int p_DosierMenge);
    
    //## auto_generated
    bool getError() const;
    
    //## auto_generated
    void setError(bool p_Error);
    
    //## auto_generated
    int getMaxTime() const;
    
    //## auto_generated
    void setMaxTime(int p_MaxTime);
    
    //## auto_generated
    int getStationsNr() const;
    
    //## auto_generated
    void setStationsNr(int p_StationsNr);
    
    //## auto_generated
    Karussell* getItsKarussell() const;
    
    //## auto_generated
    void setItsKarussell(Karussell* p_Karussell);
    
    //## auto_generated
    int getItsKolben() const;
    
    //## auto_generated
    void addItsKolben(Kolben* p_Kolben);
    
    //## auto_generated
    void removeItsKolben(Kolben* p_Kolben);
    
    //## auto_generated
    void clearItsKolben();
    
    //## auto_generated
    Tuer* getItsTuer() const;
    
    //## auto_generated
    Waage* getItsWaage() const;
    
    //## auto_generated
    void setItsWaage(Waage* p_Waage);
    
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

public :

    //## TriggeredOperation evReady()
    void evReady();
    
    ////    Attributes    ////

protected :

    int DosierMenge;		//## attribute DosierMenge
    
    bool Error;		//## attribute Error
    
    int MaxTime;		//## attribute MaxTime
    
    int StationsNr;		//## attribute StationsNr
    
    ////    Relations and components    ////
    
    Karussell* itsKarussell;		//## link itsKarussell
    
    Kolben* itsKolben[2];		//## link itsKolben
    
    Waage* itsWaage;		//## link itsWaage
    
    Tuer itsTuer;		//## classInstance itsTuer
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void __setItsKarussell(Karussell* p_Karussell);
    
    //## auto_generated
    void _setItsKarussell(Karussell* p_Karussell);
    
    //## auto_generated
    void _clearItsKarussell();
    
    //## auto_generated
    void _addItsKolben(Kolben* p_Kolben);
    
    //## auto_generated
    void _removeItsKolben(Kolben* p_Kolben);
    
    //## auto_generated
    void _clearItsKolben();
    
    ////    Framework    ////
    
    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // Betrieb:
    //## statechart_method
    inline bool Betrieb_IN() const;
    
    //## statechart_method
    void Betrieb_entDef();
    
    //## statechart_method
    void Betrieb_exit();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Betrieb_processEvent();
    
    // state_5:
    //## statechart_method
    inline bool state_5_IN() const;
    
    //## statechart_method
    void state_5_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_5_processEvent();
    
    // Zu:
    //## statechart_method
    inline bool Zu_IN() const;
    
    // Offen:
    //## statechart_method
    inline bool Offen_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Offen_handleEvent();
    
    // state_4:
    //## statechart_method
    inline bool state_4_IN() const;
    
    //## statechart_method
    void state_4_entDef();
    
    //## statechart_method
    IOxfReactive::TakeEventStatus state_4_processEvent();
    
    // Stopped:
    //## statechart_method
    inline bool Stopped_IN() const;
    
    // Running:
    //## statechart_method
    inline bool Running_IN() const;
    
    //## statechart_method
    IOxfReactive::TakeEventStatus Running_handleEvent();
    
    // Idle:
    //## statechart_method
    inline bool Idle_IN() const;

protected :

//#[ ignore
    enum Station_Enum {
        OMNonState = 0,
        Betrieb = 1,
        state_5 = 2,
        Zu = 3,
        Offen = 4,
        state_4 = 5,
        Stopped = 6,
        Running = 7,
        Idle = 8
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    int state_5_subState;
    
    int state_5_active;
    
    IOxfTimeout* state_5_timeout;
    
    int state_4_subState;
    
    int state_4_active;
    
    IOxfTimeout* state_4_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedStation : virtual public AOMInstance {
    DECLARE_REACTIVE_META(Station, OMAnimatedStation)
    
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

//#[ ignore
class evReady_Station_Event : public OMEvent {
    ////    Constructors and destructors    ////
    
public :

    evReady_Station_Event();
};
//#]

inline bool Station::rootState_IN() const {
    return true;
}

inline bool Station::Betrieb_IN() const {
    return rootState_subState == Betrieb;
}

inline bool Station::state_5_IN() const {
    return Betrieb_IN();
}

inline bool Station::Zu_IN() const {
    return state_5_subState == Zu;
}

inline bool Station::Offen_IN() const {
    return state_5_subState == Offen;
}

inline bool Station::state_4_IN() const {
    return Betrieb_IN();
}

inline bool Station::Stopped_IN() const {
    return state_4_subState == Stopped;
}

inline bool Station::Running_IN() const {
    return state_4_subState == Running;
}

inline bool Station::Idle_IN() const {
    return state_4_subState == Idle;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Station.h
*********************************************************************/
