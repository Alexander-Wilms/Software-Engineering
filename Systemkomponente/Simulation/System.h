/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: System
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/System.h
*********************************************************************/

#ifndef System_H
#define System_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include <oxf/event.h>
//## auto_generated
class Abfuellstation;

//## auto_generated
class Cachacca;

//## classInstance CaipiAutomat
class Caipisystem;

//## auto_generated
class Dosierer;

//## auto_generated
class EinAusgabe;

//## auto_generated
class Eis;

//## auto_generated
class Karussell;

//## auto_generated
class Kolben;

//## auto_generated
class Led;

//## auto_generated
class Lichtschranke;

//## auto_generated
class Limetten;

//## auto_generated
class Limettenschneider;

//## auto_generated
class Stampfer;

//## auto_generated
class Station;

//## auto_generated
class Tuer;

//## auto_generated
class Vorrat;

//## auto_generated
class Waage;

//## auto_generated
class Zucker;

//#[ ignore
#define evGlas_System_id 5801

#define evNoGlas_System_id 5802

#define evRun_System_id 5803

#define evStop_System_id 5804

#define evContinue_System_id 5805

#define evFuellen_System_id 5806

#define moveup_System_id 5807

#define movedown_System_id 5808

#define evNoLimette_System_id 5809

#define evSReady_System_id 5810

#define evReady_System_id 5811

#define evLIMReady_System_id 5812
//#]

//## package System


//## attribute GlasGewicht
const int GlasGewicht(100);

//## attribute MaxStation
const int MaxStation(6);

//## classInstance CaipiAutomat
extern Caipisystem CaipiAutomat;

//## auto_generated
void System_initRelations();

//## auto_generated
bool System_startBehavior();

//#[ ignore
class System_OMInitializer {
    ////    Constructors and destructors    ////
    
public :

    //## auto_generated
    System_OMInitializer();
    
    //## auto_generated
    ~System_OMInitializer();
};
//#]

//## event evGlas()
class evGlas : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevGlas;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evGlas();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevGlas : virtual public AOMEvent {
    DECLARE_META_EVENT(evGlas)
};
//#]
#endif // _OMINSTRUMENT

//## event evNoGlas()
class evNoGlas : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevNoGlas;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evNoGlas();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevNoGlas : virtual public AOMEvent {
    DECLARE_META_EVENT(evNoGlas)
};
//#]
#endif // _OMINSTRUMENT

//## event evRun()
class evRun : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevRun;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evRun();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevRun : virtual public AOMEvent {
    DECLARE_META_EVENT(evRun)
};
//#]
#endif // _OMINSTRUMENT

//## event evStop()
class evStop : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevStop;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evStop();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevStop : virtual public AOMEvent {
    DECLARE_META_EVENT(evStop)
};
//#]
#endif // _OMINSTRUMENT

//## event evContinue()
class evContinue : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevContinue;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evContinue();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevContinue : virtual public AOMEvent {
    DECLARE_META_EVENT(evContinue)
};
//#]
#endif // _OMINSTRUMENT

//## event evFuellen()
class evFuellen : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevFuellen;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evFuellen();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevFuellen : virtual public AOMEvent {
    DECLARE_META_EVENT(evFuellen)
};
//#]
#endif // _OMINSTRUMENT

//## event moveup()
class moveup : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedmoveup;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    moveup();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedmoveup : virtual public AOMEvent {
    DECLARE_META_EVENT(moveup)
};
//#]
#endif // _OMINSTRUMENT

//## event movedown()
class movedown : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedmovedown;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    movedown();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedmovedown : virtual public AOMEvent {
    DECLARE_META_EVENT(movedown)
};
//#]
#endif // _OMINSTRUMENT

//## event evNoLimette()
class evNoLimette : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevNoLimette;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evNoLimette();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevNoLimette : virtual public AOMEvent {
    DECLARE_META_EVENT(evNoLimette)
};
//#]
#endif // _OMINSTRUMENT

//## event evSReady()
class evSReady : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevSReady;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evSReady();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevSReady : virtual public AOMEvent {
    DECLARE_META_EVENT(evSReady)
};
//#]
#endif // _OMINSTRUMENT

//## event evReady()
class evReady : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevReady;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evReady();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevReady : virtual public AOMEvent {
    DECLARE_META_EVENT(evReady)
};
//#]
#endif // _OMINSTRUMENT

//## event evLIMReady()
class evLIMReady : public OMEvent {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedevLIMReady;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    evLIMReady();
    
    ////    Framework operations    ////
    
    //## statechart_method
    virtual bool isTypeOf(const short id) const;
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedevLIMReady : virtual public AOMEvent {
    DECLARE_META_EVENT(evLIMReady)
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/System.h
*********************************************************************/
