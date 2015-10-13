/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Caipisystem
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Caipisystem.h
*********************************************************************/

#ifndef Caipisystem_H
#define Caipisystem_H

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
//## classInstance itsCachacca
#include "Cachacca.h"
//## classInstance itsEinAusgabe
#include "EinAusgabe.h"
//## classInstance itsEis
#include "Eis.h"
//## classInstance itsKarussell
#include "Karussell.h"
//## classInstance itsLed
#include "Led.h"
//## classInstance itsLichtschranke
#include "Lichtschranke.h"
//## classInstance itsLimetten
#include "Limetten.h"
//## classInstance itsStampfer
#include "Stampfer.h"
//## classInstance itsWaage
#include "Waage.h"
//## classInstance itsZucker
#include "Zucker.h"
//## package System

//## class Caipisystem
class Caipisystem : public OMReactive {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedCaipisystem;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## operation Caipisystem()
    Caipisystem(IOxfActive* theActiveContext = 0);
    
    //## auto_generated
    ~Caipisystem();
    
    ////    Additional operations    ////
    
    //## auto_generated
    Cachacca* getItsCachacca() const;
    
    //## auto_generated
    EinAusgabe* getItsEinAusgabe() const;
    
    //## auto_generated
    Eis* getItsEis() const;
    
    //## auto_generated
    Karussell* getItsKarussell() const;
    
    //## auto_generated
    int getItsLed() const;
    
    //## auto_generated
    Lichtschranke* getItsLichtschranke() const;
    
    //## auto_generated
    Limetten* getItsLimetten() const;
    
    //## auto_generated
    Stampfer* getItsStampfer() const;
    
    //## auto_generated
    int getItsWaage() const;
    
    //## auto_generated
    Zucker* getItsZucker() const;
    
    //## auto_generated
    virtual bool startBehavior();

protected :

    //## auto_generated
    void initRelations();
    
    ////    Relations and components    ////
    
    Cachacca itsCachacca;		//## classInstance itsCachacca
    
    EinAusgabe itsEinAusgabe;		//## classInstance itsEinAusgabe
    
    Eis itsEis;		//## classInstance itsEis
    
    Karussell itsKarussell;		//## classInstance itsKarussell
    
    Led itsLed[6];		//## classInstance itsLed
    
    Lichtschranke itsLichtschranke;		//## classInstance itsLichtschranke
    
    Limetten itsLimetten;		//## classInstance itsLimetten
    
    Stampfer itsStampfer;		//## classInstance itsStampfer
    
    Waage itsWaage[6];		//## classInstance itsWaage
    
    Zucker itsZucker;		//## classInstance itsZucker
    
    ////    Framework operations    ////

public :

    //## auto_generated
    void setActiveContext(IOxfActive* theActiveContext, bool activeInstance);
    
    //## auto_generated
    virtual void destroy();
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedCaipisystem : virtual public AOMInstance {
    DECLARE_META(Caipisystem, OMAnimatedCaipisystem)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Caipisystem.h
*********************************************************************/
