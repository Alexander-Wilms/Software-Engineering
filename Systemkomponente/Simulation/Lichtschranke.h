/*********************************************************************
	Rhapsody	: 8.1.3 
	Login		: Alexander Wilms
	Component	: Systemkomponente 
	Configuration 	: Simulation
	Model Element	: Lichtschranke
//!	Generated Date	: Wed, 16, Sep 2015  
	File Path	: Systemkomponente/Simulation/Lichtschranke.h
*********************************************************************/

#ifndef Lichtschranke_H
#define Lichtschranke_H

//## auto_generated
#include <oxf/oxf.h>
//## auto_generated
#include <aom/aom.h>
//## auto_generated
#include "System.h"
//## link itsLimetten
class Limetten;

//## link itsStation
class Station;

//## package System

//## class Lichtschranke
class Lichtschranke {
    ////    Friends    ////
    
public :

#ifdef _OMINSTRUMENT
    friend class OMAnimatedLichtschranke;
#endif // _OMINSTRUMENT

    ////    Constructors and destructors    ////
    
    //## auto_generated
    Lichtschranke();
    
    //## auto_generated
    ~Lichtschranke();
    
    ////    Operations    ////
    
    //## operation check()
    bool check();
    
    ////    Additional operations    ////
    
    //## auto_generated
    Limetten* getItsLimetten() const;
    
    //## auto_generated
    void setItsLimetten(Limetten* p_Limetten);
    
    //## auto_generated
    Station* getItsStation() const;
    
    //## auto_generated
    void setItsStation(Station* p_Station);

protected :

    //## auto_generated
    void cleanUpRelations();
    
    ////    Relations and components    ////
    
    Limetten* itsLimetten;		//## link itsLimetten
    
    Station* itsStation;		//## link itsStation
};

#ifdef _OMINSTRUMENT
//#[ ignore
class OMAnimatedLichtschranke : virtual public AOMInstance {
    DECLARE_META(Lichtschranke, OMAnimatedLichtschranke)
    
    ////    Framework operations    ////
    
public :

    virtual void serializeRelations(AOMSRelations* aomsRelations) const;
};
//#]
#endif // _OMINSTRUMENT

#endif
/*********************************************************************
	File Path	: Systemkomponente/Simulation/Lichtschranke.h
*********************************************************************/
