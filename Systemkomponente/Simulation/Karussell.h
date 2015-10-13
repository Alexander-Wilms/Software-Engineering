/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Karussell
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Karussell.h
*********************************************************************/

#ifndef Karussell_H
#define Karussell_H

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
//## link itsLed
class Led;

//## link itsStation
class Station;

//## link itsWaage
class Waage;

//## package System

//## class Karussell
class Karussell : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedKarussell;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Karussell(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Karussell();
    
    ////    Operations    ////
    
    //## operation GlaeserDrauf()
    int GlaeserDrauf();
    
    //## operation addWaage(int,int)
    void addWaage(int aWaage, int aMenge);
    
    //## operation clearBrutto(int)
    void clearBrutto(int aWaage);
    
    //## operation drehen()
    void drehen();
    
    //## operation getBrutto(int)
    int getBrutto(int aWaage);
    
    //## operation getNetto(int)
    int getNetto(int aWaage);
    
    //## operation setTara(int)
    void setTara(int aWaage);
    
    //## operation updateLED()
    void updateLED();
    
    ////    Additional operations    ////
    
    //## auto_generated
    bool getDreht() const;
    
    //## auto_generated
    void setDreht(bool p_dreht);
    
    //## auto_generated
    bool getJemalsgedreht() const;
    
    //## auto_generated
    void setJemalsgedreht(bool p_jemalsgedreht);
    
    //## auto_generated
    int getItsLed() const;
    
    //## auto_generated
    void addItsLed(Led* p_Led);
    
    //## auto_generated
    void removeItsLed(Led* p_Led);
    
    //## auto_generated
    void clearItsLed();
    
    //## auto_generated
    int getItsStation() const;
    
    //## auto_generated
    void addItsStation(Station* p_Station);
    
    //## auto_generated
    void removeItsStation(Station* p_Station);
    
    //## auto_generated
    void clearItsStation();
    
    //## auto_generated
    int getItsWaage() const;
    
    //## auto_generated
    void addItsWaage(Waage* p_Waage);
    
    //## auto_generated
    void removeItsWaage(Waage* p_Waage);
    
    //## auto_generated
    void clearItsWaage();
    
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
    
    bool dreht;		//## attribute dreht
    
    bool jemalsgedreht;		//## attribute jemalsgedreht
    
    ////    Relations and components    ////
    
    Led* itsLed[6];		//## link itsLed
    
    Station* itsStation[6];		//## link itsStation
    
    Waage* itsWaage[6];		//## link itsWaage
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void _addItsStation(Station* p_Station);
    
    //## auto_generated
    void _removeItsStation(Station* p_Station);
    
    //## auto_generated
    void _clearItsStation();
    
    ////    Framework    ////
    
    // rootState:
    //## statechart_method
    inline bool rootState_IN() const;
    
    //## statechart_method
    virtual void rootState_entDef();
    
    //## statechart_method
    virtual IOxfReactive::TakeEventStatus rootState_processEvent();
    
    // idle:
    //## statechart_method
    inline bool idle_IN() const;

protected :

//#[ ignore
    enum Karussell_Enum {
        OMNonState = 0,
        idle = 1
    };
    
    int rootState_subState;
    
    int rootState_active;
    
    IOxfTimeout* rootState_timeout;
//#]
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedKarussell : virtual public AOMInstance {
    DECLARE_REACTIVE_META(Karussell, OMAnimatedKarussell)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeAttributes(AOMSAttributes* aomsAttributes) const;
    
    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
    
    //## statechart_method
    void rootState_serializeStates(AOMSState* aomsState) const;
    
    //## statechart_method
    void idle_serializeStates(AOMSState* aomsState) const;
};
//#]
#endif // _OMINSTRUMENT

inline bool Karussell::rootState_IN() const {
    return true;
}

inline bool Karussell::idle_IN() const {
    return rootState_subState == idle;
}

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Karussell.h
*********************************************************************/
