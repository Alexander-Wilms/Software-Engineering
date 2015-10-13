I-Logix-RPY-Archive version 8.10.0 C++ 6930133
{ IProject 
	- _id = GUID a585e1b1-03bd-4e0f-b7ea-5dbb312e35db;
	- _myState = 8192;
	- _name = "Caipi";
	- _modifiedTimeWeak = 1.30.2015::13:50:43;
	- _lastID = 1;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "System.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "System";
		- _id = GUID df584e7e-050b-41c4-88fe-3f798a129e39;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "Systemkomponente.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "Systemkomponente";
		- _id = GUID 89557f6c-fafa-457f-a11a-f02f24fe3d66;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 5;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 14;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "6";
			- _count = 1;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ ISubsystem 
			- fileName = "System";
			- _id = GUID df584e7e-050b-41c4-88fe-3f798a129e39;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 2;
		- value = 
		{ IDiagram 
			- _id = GUID 8f4c50d7-c3f1-441a-8dd9-e92f2a03116b;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 6;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Aggregation";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Composition";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 4;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "128,128,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 2;
									- value = 
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "grid_snap";
										- _Value = "True";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Overview";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "1.25.2015::13:30:21";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 3e37cb01-191d-4c57-b43a-b002e4de1aac;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 8f4c50d7-c3f1-441a-8dd9-e92f2a03116b;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 34;
				{ CGIClass 
					- _id = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID e3f87dd4-ea53-404c-8c07-a660554e67e3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 8774f818-f354-4c57-b10f-fd2cd7f21ff4;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 3d3b507b-0a7f-49ee-a2b9-ce30bf4f0d85;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 4de125a6-64e7-4e9b-ae12-d19fb599a16d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 105;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Caipisystem";
						- _id = GUID 05345632-89dc-4b54-a9d6-8d8a7fcaf4fe;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Caipisystem";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.100671 0 0 0.0419214 491.698 24.8908 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 3 265  3 1410  1195 1410  1195 265  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 1d56d2d2-2d20-451e-a6f3-21bce328e48c;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID d4e04d6c-facb-41ba-bc9d-169520829805;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID e8d71d06-6440-4202-87f3-a7852ececdc1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 105;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Karussell";
						- _id = GUID 1d40557e-9c64-4e93-87d1-d2ac8b05951b;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Karussell";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.100671 0 0 0.0419214 1115.7 360.891 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 3 265  3 1410  1195 1410  1195 265  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 8ba83702-71dc-4948-a0da-2984527bf9e9;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID d3c330b5-6523-47f6-9296-c41e72c1c30b;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 476eaa6e-fdce-4691-a754-4327b5fd7713;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 105;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "EinAusgabe";
						- _id = GUID 691ac2da-1045-480b-83d4-54c4dbfc3c8e;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "EinAusgabe";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.100671 0 0 0.0419214 575.698 360.891 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 3 265  3 1410  1195 1410  1195 265  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 5a467a93-43db-4b64-9ec3-3f26daa98926;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 331d5b75-8cd2-4043-88a2-50612842b8c8;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID cfa7c82f-b87f-4722-b6b9-ebdf95c7ca24;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 105;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Abfuellstation";
						- _id = GUID 9d88b57f-cce2-43ca-85ab-976eb28aa468;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Abfuellstation";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.100671 0 0 0.0419214 395.698 360.891 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 3 265  3 1410  1195 1410  1195 265  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID b5337271-ab2a-40d1-8958-96c19df6ef23;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 6ad305e7-66af-4f2d-9cf0-8fffc6a16696;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 05b0bf8e-8757-4be6-a63b-3752398e4bf8;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 105;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Stampfer";
						- _id = GUID f3b374c4-07b7-4c42-bc55-ce9b4ac9c2fe;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Stampfer";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.100671 0 0 0.0419214 935.698 360.891 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 3 265  3 1410  1195 1410  1195 265  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID ac594457-a1e0-473f-bf9b-c40487fd13da;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 9e11cbdf-4b26-41c8-99f3-6eb522c8895e;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Station";
						- _id = GUID 5113e960-1733-4da6-97e8-2735eb576097;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Station";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 671.773 249.925 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 9b44a48b-8ad9-4b81-8bf6-bbd3bf95d981;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 1;
								- value = 
								{ IHandle 
									- _m2Class = "IAttribute";
									- _filename = "";
									- _subsystem = "System";
									- _class = "Station";
									- _name = "StationsNr";
									- _id = GUID b88dbf60-cc2f-49a2-9d5a-c603f6011bf6;
								}
							}
						}
						{ CGICompartment 
							- _id = GUID af0b0069-2c2e-4ada-8111-753b0ece35f7;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 7ad5aede-43a8-4acd-aa1d-f490fd5c639f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "EinAusgabe";
						- _name = "Station";
						- _id = GUID 44d78e31-197c-4f84-b6af-1dbfde4a9c49;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 476eaa6e-fdce-4691-a754-4327b5fd7713;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 636 342  720 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 599 265 ;
					- m_TargetPort = 426 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID ad9f83b2-f686-4965-82a4-68c5c63e588e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Abfuellstation";
						- _name = "Station";
						- _id = GUID 0ae6198b-c0ab-4977-8cbc-340e429cd2f3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID cfa7c82f-b87f-4722-b6b9-ebdf95c7ca24;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 456 342  720 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 599 265 ;
					- m_TargetPort = 426 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 9db19e77-5920-44f7-9ea0-0531cc2b47ed;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Stampfer";
						- _name = "Station";
						- _id = GUID ee1c77bd-b17e-4d38-bc6f-c7529ce75185;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 05b0bf8e-8757-4be6-a63b-3752398e4bf8;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 996 342  720 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 599 265 ;
					- m_TargetPort = 426 1451 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIAssociationEnd 
					- _id = GUID 5964da34-8c2f-4775-b61b-744350a9b618;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Karussell";
						- _name = "itsStation";
						- _id = GUID 25d45ef6-3327-4293-9e10-c13d2a7cf94a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID e8d71d06-6440-4202-87f3-a7852ececdc1;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 1140 342  780 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 241 265 ;
					- m_TargetPort = 955 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "itsKarussell";
						- _id = GUID 8002ad26-68aa-4e10-acc0-eed868523673;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 960.5 341.500000000001  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "6";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 960.5 341.500000000001  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID 418d288e-4206-4adc-9957-fd228b998b73;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Waage";
						- _id = GUID ce975fb8-fdd5-4724-83e0-711e903e6e20;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Waage";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 1031.77 249.925 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID c05204e3-c704-4fda-8c2a-4556ca67f598;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID fd68bbb6-26f4-4cc7-b106-c61d97a0ab14;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID c987783c-73f3-43cb-bc76-75414c086c63;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Led";
						- _id = GUID 695509f9-dcf8-450e-af93-4dfb95838c8d;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Led";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 1211.77 249.925 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID b82b651b-94bb-46aa-abed-0b7f90f8f8fa;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID b208baa3-632b-4be7-8d2c-8162d6ce94b4;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID a0a1f9a6-3afd-4417-817e-8b51257d144f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Karussell";
						- _name = "itsWaage";
						- _id = GUID 67af3087-6f0d-470e-8065-a5b1cadfa7f8;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID e8d71d06-6440-4202-87f3-a7852ececdc1;
					- m_sourceType = 'F';
					- m_pTarget = GUID 418d288e-4206-4adc-9957-fd228b998b73;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 1176 342  1092 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 599 265 ;
					- m_TargetPort = 532 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "6";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 370 341  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID aa8343ba-3d27-48e5-9e8e-ef5d6edb2954;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Karussell";
						- _name = "itsLed";
						- _id = GUID 6a3ebbaa-4b19-47ee-8bdb-5cc74166fd3b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID e8d71d06-6440-4202-87f3-a7852ececdc1;
					- m_sourceType = 'F';
					- m_pTarget = GUID c987783c-73f3-43cb-bc76-75414c086c63;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 1224 342  1272 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 1076 265 ;
					- m_TargetPort = 532 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "6";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 1246 341  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID dcfa5615-7934-42e1-817d-bb2ce12a7dc5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Tuer";
						- _id = GUID 8d81cc7c-8684-4d68-bff0-ffd7d3c9a8d1;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Tuer";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 311.773 21.9251 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 765b03c2-08c8-4142-b368-1832bd91803e;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID c95975fb-27d1-4259-82cc-53f265b1b871;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID 5d2458fc-94f0-4c14-a272-71e5aa5ec4e0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Zucker";
						- _id = GUID 20545060-85e9-4cc4-a473-41e458699746;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Zucker";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0534759 755.773 462.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID fa6c2ebf-f636-4502-a40f-cf2e168350b5;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 59d9051f-047a-4d05-876c-eb63beff806b;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 00ed70f5-9a11-4532-9a91-473f262504d5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Zucker";
						- _name = "Abfuellstation";
						- _id = GUID 34271da1-20cd-4579-a993-b6a528f1ddf2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5d2458fc-94f0-4c14-a272-71e5aa5ec4e0;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfa7c82f-b87f-4722-b6b9-ebdf95c7ca24;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 816 450  504 450  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 1076 1410 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 5e67a10a-4947-42cc-a299-a403f30c6c4c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Cachacca";
						- _id = GUID b0553e09-cdbc-41d6-baf0-d4f8fed969b3;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Cachacca";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0534759 395.773 462.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 4ffe8a1b-1d3b-431c-9b9f-3510ca771d6a;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 904feb74-afc7-4d83-a3e7-a527ddd89368;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 0cb5790c-00cd-4353-a6f6-a0de8b73f32b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Cachacca";
						- _name = "Abfuellstation";
						- _id = GUID d4b3366a-91cd-491e-9e58-2b36924baa13;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 5e67a10a-4947-42cc-a299-a403f30c6c4c;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfa7c82f-b87f-4722-b6b9-ebdf95c7ca24;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 456 450  504 450  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 1076 1410 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 5e4c2ee1-25ae-48bf-a72c-4e6aab0f51e1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Vorrat";
						- _id = GUID 7d0a1c46-8573-409f-a462-22b3c3e88378;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Vorrat";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 215.773 249.925 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID f2ebd615-f925-4038-bc4e-fc6ee22e08b6;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID b79f150d-9c47-4b44-be01-5a35525e7d90;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIClass 
					- _id = GUID df416b68-36bb-47fa-8788-640fd6413497;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Dosierer";
						- _id = GUID 5ef5d3ba-1634-4c72-ba82-4a82cceef758;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Dosierer";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 215.773 357.925 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID de3c81d5-1484-4336-8941-535d0a401017;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID ee72f38a-4dae-4647-a15e-57ee0ed8574c;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID fa116883-d300-4afc-bd11-bc0692c16904;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Dosierer";
						- _name = "itsVorrat";
						- _id = GUID f15c13f8-037c-48cd-a4da-eb674d4ef26e;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 0;
					- m_pSource = GUID df416b68-36bb-47fa-8788-640fd6413497;
					- m_sourceType = 'F';
					- m_pTarget = GUID 5e4c2ee1-25ae-48bf-a72c-4e6aab0f51e1;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 531 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIAssociationEnd 
					- _id = GUID e6070870-9e29-48c9-9588-de4f52ed30c1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Dosierer";
						- _name = "itsStation";
						- _id = GUID 704d4e0b-a0e0-4d56-8f8c-8d7f94fd2e31;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 0;
					- m_pSource = GUID df416b68-36bb-47fa-8788-640fd6413497;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 312 342  684 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 849 329 ;
					- m_TargetPort = 108 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 495.0625 341.55  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID 9e1785be-2671-485d-a17a-a46e12794900;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Limetten";
						- _id = GUID 7621aa2f-54d3-44f4-833b-85f8fddc75b9;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Limetten";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0534759 215.773 462.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID ec5afcb5-bd95-425a-bb79-c2eea8c5bfb6;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID a3b3ebe1-db95-431f-b084-fbb4ed55397e;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 82276491-d771-402b-a1a8-8cdc06345a14;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Limetten";
						- _name = "Abfuellstation";
						- _id = GUID 3dbdd7d1-a454-4d8c-8011-5492c023b476;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 9e1785be-2671-485d-a17a-a46e12794900;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfa7c82f-b87f-4722-b6b9-ebdf95c7ca24;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 276 450  504 450  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 1076 1410 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID f745e453-348e-4ab4-a928-409a758bee20;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Eis";
						- _id = GUID 7828c6bc-49e9-4a92-8673-51be192e80bc;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Eis";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0534759 35.7734 462.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID d90ab2e6-aeff-4371-b619-fcc0cd10baac;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 143e665d-3af0-4a00-9902-b3ddb5d18182;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID e320352d-6f07-4459-8647-926f311d8d5f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Eis";
						- _name = "Abfuellstation";
						- _id = GUID c73a30f8-4e9d-4441-9c17-3ed2a8d3cbb6;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID f745e453-348e-4ab4-a928-409a758bee20;
					- m_sourceType = 'F';
					- m_pTarget = GUID cfa7c82f-b87f-4722-b6b9-ebdf95c7ca24;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 96 450  504 450  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 532 329 ;
					- m_TargetPort = 1076 1410 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIClass 
					- _id = GUID 8c29518c-6c1f-4bdc-8967-d9ac24e6efda;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Lichtschranke";
						- _id = GUID c7be984f-a861-4e28-86ac-3f42d502715a;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Lichtschranke";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0427807 755.773 357.925 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 62c62517-bb8e-4718-96ea-fac3d4079aef;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 402c1b95-b22f-42b6-b40c-dfcc16f22855;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 02cb8417-4007-4fa1-aa1e-4b5271ee3d60;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Lichtschranke";
						- _name = "itsStation";
						- _id = GUID 333ead29-faf4-4d2a-814a-14857524a33b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 8c29518c-6c1f-4bdc-8967-d9ac24e6efda;
					- m_sourceType = 'F';
					- m_pTarget = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 816 342  744 342  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 637 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "";
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 780.5 342  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nVerticalSpacing = 7;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = type_122;
				}
				{ CGIClass 
					- _id = GUID 8ca1824e-8314-4d87-87a8-56199cacd503;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Kolben";
						- _id = GUID 328ba5c2-a7db-4add-927b-3af2fccbe4c8;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Kolben";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.113314 0 0 0.0534759 671.773 126.406 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID a5f67b4c-3695-48df-9504-9a85cd7db2f2;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 98b550e9-ccab-4d0e-b53c-2bd846b1207e;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 5ba4798c-6d39-4caf-90cd-49090c1429ce;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "itsKolben";
						- _id = GUID 48f9c876-3e2c-48f1-a24f-e0a32933bcae;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_bIsPreferencesInitialized = 0;
					- m_pSource = GUID b5bc2ed9-34a5-4335-9c58-65d6a742a6e3;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8ca1824e-8314-4d87-87a8-56199cacd503;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 531 329 ;
					- m_TargetPort = 531 1451 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Kolben";
						- _name = "itsStation";
						- _id = GUID 8f48350b-188e-46e5-8bc8-5a0e0f38742a;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID 106af007-640e-4f10-aa1f-91f14279186f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Class";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 87;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "Limettenschneider";
						- _id = GUID 2bf4b1bb-b775-4d33-b1e2-9f617a77c0f0;
					}
					- m_pParent = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
					- m_name = { CGIText 
						- m_str = "Limettenschneider";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.11898 0 0 0.106952 863.762 72.8128 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 218be491-050c-43d6-bec9-1790ca5c40af;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID 10f5db1d-be07-4a7d-9a90-199cea4dde28;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID 0c76ece1-2bf9-466d-a4e2-6dddd7540b7e;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Limettenschneider";
						- _name = "Kolben";
						- _id = GUID c67b4141-e604-43ca-bcc7-6c46ee32a2ca;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4104;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 106af007-640e-4f10-aa1f-91f14279186f;
					- m_sourceType = 'F';
					- m_pTarget = GUID 8ca1824e-8314-4d87-87a8-56199cacd503;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 2 1002 ;
					- m_TargetPort = 955 1002 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 1a78e934-2a4c-4f76-8e79-6b70c2d6eef2;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "System.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "System";
				- _id = GUID df584e7e-050b-41c4-88fe-3f798a129e39;
			}
		}
		{ IDiagram 
			- _id = GUID 771341a6-d504-481f-9864-76f8e926d505;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Tahoma";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "8";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Weight@Child.NameCompartment@Name";
										- _Value = "700";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "109,163,217";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Systemview";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "1.23.2015::15:57:0";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 1e2a66ee-d69c-4f7e-8ac9-a9b3689bed2f;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 771341a6-d504-481f-9864-76f8e926d505;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 2;
				{ CGIClass 
					- _id = GUID a912e45f-89d6-4fdf-bdae-0be363a9bdb6;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID e3f87dd4-ea53-404c-8c07-a660554e67e3;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID 8af1e19b-103c-478c-adee-afd590113496;
							- m_name = "Attribute";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
						{ CGICompartment 
							- _id = GUID d8762ddb-ae1a-4c71-be1d-81a002405c83;
							- m_name = "Operation";
							- m_displayOption = Explicit;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
							- Items = { IRPYRawContainer 
								- size = 0;
							}
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIObjectInstance 
					- _id = GUID 4663f0e6-7bc6-46d1-a09d-1987f726a878;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "ObjectModelGe";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Object";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Compartments";
												- _Value = "";
												- _Type = MultiLine;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 106;
					- m_pModelObject = { IHandle 
						- _m2Class = "IPart";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "TopLevel";
						- _name = "CaipiAutomat";
						- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
					}
					- m_pParent = GUID a912e45f-89d6-4fdf-bdae-0be363a9bdb6;
					- m_name = { CGIText 
						- m_str = "CaipiAutomat:Caipisystem";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.175637 0 0 0.104278 39.6487 5.69253 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=OperationListCompartment>";
					- Compartments = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ CGICompartment 
							- _id = GUID ed3a0617-caac-446d-99bd-813c0afe4cdc;
							- m_name = "Attribute";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
						{ CGICompartment 
							- _id = GUID 734fb644-e652-4015-8762-3cff786f4965;
							- m_name = "Operation";
							- m_displayOption = Public;
							- m_bShowInherited = 0;
							- m_bOrdered = 0;
						}
					}
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
					- m_multiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID a912e45f-89d6-4fdf-bdae-0be363a9bdb6;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "System.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "System";
				- _id = GUID df584e7e-050b-41c4-88fe-3f798a129e39;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "Systemkomponente";
			- _id = GUID 89557f6c-fafa-457f-a11a-f02f24fe3d66;
		}
	}
	- PanelDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IPanelDiagram 
			- _id = GUID 4f26ca25-c7a8-4d92-8d21-c80d78dabb0b;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 2;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "ButtonArray";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,50";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "FreeText";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "HorzAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Multiline";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "VertAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Wordbreak";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PushButton";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,50";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Rectangle";
								- Properties = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
						}
					}
					{ IPropertySubject 
						- _Name = "General";
						- Metaclasses = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Graphics";
								- Properties = { IRPYRawContainer 
									- size = 3;
									- value = 
									{ IProperty 
										- _Name = "MaintainWindowContent";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "PanelControlTypeBindingDisplay";
										- _Value = "All";
										- _Type = Enum;
										- _ExtraTypeInfo = "All,PredefinedOnly";
									}
									{ IProperty 
										- _Name = "grid_display";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
						}
					}
				}
			}
			- _name = "GUI";
			- _modifiedTimeWeak = 1.2.1990::0:0:0;
			- _lastModifiedTime = "1.25.2015::12:17:0";
			- _graphicChart = { CGIClassChart 
				- _id = GUID 3a467414-b256-40bc-98fd-9d9cafe7cee8;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IPanelDiagram";
					- _id = GUID 4f26ca25-c7a8-4d92-8d21-c80d78dabb0b;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 57;
				{ CGIBox 
					- _id = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_type = 215;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "System.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "System";
						- _id = GUID df584e7e-050b-41c4-88fe-3f798a129e39;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIFreeShape 
					- _id = GUID bfdbc8ee-5cef-42eb-9dd4-51bb7055d1ba;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Rectangle";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Fill.FillColor";
												- _Value = "192,220,192";
												- _Type = Color;
											}
											{ IProperty 
												- _Name = "Line.LineColor";
												- _Value = "166,202,240";
												- _Type = Color;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 185;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1.29128 0 0 6.00991 -85.3142 -494.853 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 159 86  595 86  595 187  159 187  ;
				}
				{ CGIMFCCtrl 
					- _id = GUID 6389b5c8-3357-422e-b21c-afdd9182d33d;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evNoGlas()";
						- _id = GUID a299d62f-0336-4d8a-94b9-203f40439c92;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noGlas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 236 529.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEinAusgabe.evNoGlas";
					- m_csName = "noGlas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEinAusgabe";
							- _id = GUID 874ab16f-1641-4a0f-8527-bdec5b0ac4fe;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIActiveX 
					- _id = GUID 461d37ee-d235-4d47-9a5f-ccc61c4ebad3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Led";
						- _name = "On";
						- _id = GUID 64444359-66bd-4d35-a057-97f287ca4fc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "EinAus";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  51 -9  51 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 183 156 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 244 313.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLed[0].On";
					- m_csName = "EinAus";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLed";
							- _id = GUID 0708781d-69fb-4775-8981-802ca12583e4;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID b45fc930-3344-4b7d-865a-9d8d933769a3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Led";
						- _name = "On";
						- _id = GUID 64444359-66bd-4d35-a057-97f287ca4fc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Zucker";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 328 316.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLed[1].On";
					- m_csName = "Zucker";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLed";
							- _id = GUID 0708781d-69fb-4775-8981-802ca12583e4;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 0965fc94-5cdd-44ae-ab06-20f6d90824ee;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Led";
						- _name = "On";
						- _id = GUID 64444359-66bd-4d35-a057-97f287ca4fc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Limette";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 398 316.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLed[2].On";
					- m_csName = "Limette";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLed";
							- _id = GUID 0708781d-69fb-4775-8981-802ca12583e4;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 02fcc658-357f-4030-bb3d-11957d0e550f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Led";
						- _name = "On";
						- _id = GUID 64444359-66bd-4d35-a057-97f287ca4fc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Cachacca";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 540 316.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLed[4].On";
					- m_csName = "Cachacca";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLed";
							- _id = GUID 0708781d-69fb-4775-8981-802ca12583e4;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 2540ac5a-156a-4160-9526-8bef12624f63;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Led";
						- _name = "On";
						- _id = GUID 64444359-66bd-4d35-a057-97f287ca4fc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Eis";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 611 316.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLed[5].On";
					- m_csName = "Eis";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLed";
							- _id = GUID 0708781d-69fb-4775-8981-802ca12583e4;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIFreeText 
					- _id = GUID cc193804-e9b5-4b91-a259-bbf80b031de6;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "FreeText";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Font.Size";
												- _Value = "20";
												- _Type = Int;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 114 -71 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 205 102  243 102  243 120  205 120  ;
					- m_text = "BedienPanel";
				}
				{ CGIActiveX 
					- _id = GUID fad3d0f8-3544-43ad-8dbb-df8f58228ec1;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;49152;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;300;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Waage0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 169 582 ;
						- m_nHorizontalSpacing = 46;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.00139443 125 663.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[0].Brutto";
					- m_csName = "Waage0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 4d2cbf47-f342-4cb5-b771-8fa12dfc7644;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;49152;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8,25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0,7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;300;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0,2;RelativeHeight;0,9;RelativeWidth;0,9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Waage1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 272 582 ;
						- m_nHorizontalSpacing = 46;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.00139443 228 663.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[1].Brutto";
					- m_csName = "Waage1";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID f1d248bf-63e8-481a-9955-ec4a2190a208;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;49152;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8,25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0,7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;300;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0,2;RelativeHeight;0,9;RelativeWidth;0,9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Waage2";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 375 582 ;
						- m_nHorizontalSpacing = 46;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.00139443 331 663.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[2].Brutto";
					- m_csName = "Waage2";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 3724a1b9-4388-4a2d-b274-3464919c2dfb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;49152;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8,25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0,7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;300;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0,2;RelativeHeight;0,9;RelativeWidth;0,9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Waage3";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 478 582 ;
						- m_nHorizontalSpacing = 46;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.00139443 434 663.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[3].Brutto";
					- m_csName = "Waage3";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID a2519339-ddbc-4f6b-94f7-34417580d71b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;49152;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8,25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0,7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;300;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0,2;RelativeHeight;0,9;RelativeWidth;0,9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Waage4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 581 582 ;
						- m_nHorizontalSpacing = 46;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.00139443 537 663.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[4].Brutto";
					- m_csName = "Waage4";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 4ad05434-4bee-476e-94ea-5a995905734b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;49152;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8,25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0,7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;300;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0,2;RelativeHeight;0,9;RelativeWidth;0,9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Waage5";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  59 -9  59 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 684 582 ;
						- m_nHorizontalSpacing = 46;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.00139443 640 663.553 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[5].Brutto";
					- m_csName = "Waage5";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 235e3f9e-dc85-4564-9112-19c66a890de2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;IconSet;9;State;0;UserInteractionEnabled;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Tuer";
						- _name = "Zustand";
						- _id = GUID 73910c43-364e-4638-bce6-6cb214c1b969;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "onoff";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 229 356.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEinAusgabe.itsTuer.Zustand";
					- m_csName = "onoff";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Station";
							- _name = "itsTuer";
							- _id = GUID 76c0e06d-2ad0-4222-b88c-3a0576999da0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEinAusgabe";
							- _id = GUID 874ab16f-1641-4a0f-8527-bdec5b0ac4fe;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID fbad0a1c-5423-4ab7-adf1-80ad74946dad;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;IconSet;9;State;0;UserInteractionEnabled;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Tuer";
						- _name = "Zustand";
						- _id = GUID 73910c43-364e-4638-bce6-6cb214c1b969;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "onoff";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  39 -9  39 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 303 199 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 309 359.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsZucker.itsTuer.Zustand";
					- m_csName = "onoff";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Station";
							- _name = "itsTuer";
							- _id = GUID 76c0e06d-2ad0-4222-b88c-3a0576999da0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsZucker";
							- _id = GUID a06bf8e2-5a90-4966-b2ba-c4a60def2535;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 5ff9e9b8-c561-4005-82fc-d2dd73294401;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;IconSet;9;State;0;UserInteractionEnabled;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Tuer";
						- _name = "Zustand";
						- _id = GUID 73910c43-364e-4638-bce6-6cb214c1b969;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "onoff";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 379 359.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.itsTuer.Zustand";
					- m_csName = "onoff";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Station";
							- _name = "itsTuer";
							- _id = GUID 76c0e06d-2ad0-4222-b88c-3a0576999da0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID eebd70b2-0a50-40c8-9ac6-e289e228720d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;IconSet;9;State;0;UserInteractionEnabled;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Tuer";
						- _name = "Zustand";
						- _id = GUID 73910c43-364e-4638-bce6-6cb214c1b969;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "onoff";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 521 359.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsCachacca.itsTuer.Zustand";
					- m_csName = "onoff";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Station";
							- _name = "itsTuer";
							- _id = GUID 76c0e06d-2ad0-4222-b88c-3a0576999da0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsCachacca";
							- _id = GUID eafd0249-b303-4b25-82eb-c2b1ce8f1c46;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d0a6547a-f4af-4311-9f5e-b132bd15e917;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;IconSet;9;State;0;UserInteractionEnabled;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Tuer";
						- _name = "Zustand";
						- _id = GUID 73910c43-364e-4638-bce6-6cb214c1b969;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "onoff";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 592 359.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEis.itsTuer.Zustand";
					- m_csName = "onoff";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Station";
							- _name = "itsTuer";
							- _id = GUID 76c0e06d-2ad0-4222-b88c-3a0576999da0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEis";
							- _id = GUID 59eea1c6-6535-47c5-af1f-48e41bc84559;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 006abf14-c0de-401f-b6fb-e4006b4c3d92;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;-1;BlinkingTimeMillisec;300;Color;2;State;0;Style;5;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "Error";
						- _id = GUID 694f5f63-4033-4697-9197-693188cd2f8c;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  37 -9  37 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 189 276 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 243 433.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEinAusgabe.Error";
					- m_csName = "Error";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEinAusgabe";
							- _id = GUID 874ab16f-1641-4a0f-8527-bdec5b0ac4fe;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 150cf171-0c33-4925-813e-b3b461f37a28;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;-1;BlinkingTimeMillisec;300;Color;2;State;0;Style;5;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "Error";
						- _id = GUID 694f5f63-4033-4697-9197-693188cd2f8c;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 328 436.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsZucker.Error";
					- m_csName = "Error";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsZucker";
							- _id = GUID a06bf8e2-5a90-4966-b2ba-c4a60def2535;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID fe8e553b-c945-4252-adf3-4f4eacd1e7cb;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;-1;BlinkingTimeMillisec;300;Color;2;State;0;Style;5;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "Error";
						- _id = GUID 694f5f63-4033-4697-9197-693188cd2f8c;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 399 436.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.Error";
					- m_csName = "Error";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID f5621f77-2365-40d3-8341-fc0941732fba;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;-1;BlinkingTimeMillisec;300;Color;2;State;0;Style;5;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "Error";
						- _id = GUID 694f5f63-4033-4697-9197-693188cd2f8c;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 543 436.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsCachacca.Error";
					- m_csName = "Error";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsCachacca";
							- _id = GUID eafd0249-b303-4b25-82eb-c2b1ce8f1c46;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 64104c00-f165-48ef-bef8-344c31d3c593;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;-1;BlinkingTimeMillisec;300;Color;2;State;0;Style;5;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "Error";
						- _id = GUID 694f5f63-4033-4697-9197-693188cd2f8c;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 615 436.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEis.Error";
					- m_csName = "Error";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEis";
							- _id = GUID 59eea1c6-6535-47c5-af1f-48e41bc84559;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 9c58d4a0-a56d-495e-9771-7928d4568344;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evFuellen()";
						- _id = GUID 23478db0-1db7-4361-a0be-dd70e7950e55;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "fuellen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  51 -9  51 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 295 313 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 314 473.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsZucker.evFuellen";
					- m_csName = "fuellen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsZucker";
							- _id = GUID a06bf8e2-5a90-4966-b2ba-c4a60def2535;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 25731d20-3d7e-411c-ab87-9badb438ff8e;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evFuellen()";
						- _id = GUID 23478db0-1db7-4361-a0be-dd70e7950e55;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "fuellen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 535 473.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsCachacca.evFuellen";
					- m_csName = "fuellen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsCachacca";
							- _id = GUID eafd0249-b303-4b25-82eb-c2b1ce8f1c46;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 22fb2060-304b-4af3-bbd3-baaef6c26ff9;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evFuellen()";
						- _id = GUID 23478db0-1db7-4361-a0be-dd70e7950e55;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "fuellen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 601 473.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEis.evFuellen";
					- m_csName = "fuellen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEis";
							- _id = GUID 59eea1c6-6535-47c5-af1f-48e41bc84559;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 65aadacb-c024-4203-82ad-6302a23444e8;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "EinAusgabe";
						- _name = "evGlas()";
						- _id = GUID 69f5c2ca-6e08-4db7-9dd0-56c579a4f281;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Glas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 236 472.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEinAusgabe.evGlas";
					- m_csName = "Glas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEinAusgabe";
							- _id = GUID 874ab16f-1641-4a0f-8527-bdec5b0ac4fe;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIFreeText 
					- _id = GUID 8ca095c9-23ed-4656-a394-4c722794165a;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -548 238 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 692 158  739 158  739 176  692 176  ;
					- m_text = "T\ür auf";
				}
				{ CGIFreeText 
					- _id = GUID 7721b4cc-a835-429b-bb64-b13730ce9465;
					- m_type = 189;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 1 0 0 1 -548 153 ;
					- m_bIsPreferencesInitialized = 1;
					- m_points = 4 692 158  730 158  730 176  692 176  ;
					- m_text = "T\ür zu";
				}
				{ CGIMFCCtrl 
					- _id = GUID 755d4d20-9213-45d7-a447-8f8ac4fac22a;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evNoGlas()";
						- _id = GUID a299d62f-0336-4d8a-94b9-203f40439c92;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noGlas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 316 533.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsZucker.evNoGlas";
					- m_csName = "noGlas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsZucker";
							- _id = GUID a06bf8e2-5a90-4966-b2ba-c4a60def2535;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 4d083bb2-759f-4063-8448-fb55a07912bd;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evNoGlas()";
						- _id = GUID a299d62f-0336-4d8a-94b9-203f40439c92;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noGlas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 387 529.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.evNoGlas";
					- m_csName = "noGlas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 2cb18047-e832-4426-bcf5-ce5d27d24fd5;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evNoGlas()";
						- _id = GUID a299d62f-0336-4d8a-94b9-203f40439c92;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noGlas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 537 533.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsCachacca.evNoGlas";
					- m_csName = "noGlas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsCachacca";
							- _id = GUID eafd0249-b303-4b25-82eb-c2b1ce8f1c46;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 89f1e912-c679-4bbd-84a4-6a601413a822;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evNoGlas()";
						- _id = GUID a299d62f-0336-4d8a-94b9-203f40439c92;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noGlas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 601 532.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEis.evNoGlas";
					- m_csName = "noGlas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEis";
							- _id = GUID 59eea1c6-6535-47c5-af1f-48e41bc84559;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIActiveX 
					- _id = GUID dd26d36f-6108-40fe-887d-37dc9cab19b7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;-2147483645;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;100;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;
";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Vorrat";
						- _name = "VorhandenerVorrat";
						- _id = GUID abc9a43b-c007-4a49-baee-c20a7f42bfc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Vorrat";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 3 1  53 1  53 19  3 19  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 43 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.000662354 313 208.738 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsZucker.itsVorrat.VorhandenerVorrat";
					- m_csName = "Vorrat";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Abfuellstation";
							- _name = "itsVorrat";
							- _id = GUID 69d6b1ae-36e1-4768-89d5-83835f4db3c7;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsZucker";
							- _id = GUID a06bf8e2-5a90-4966-b2ba-c4a60def2535;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d67b6a93-e9f3-4555-a6f0-f1128980af5c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;-2147483645;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;100;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;
";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Vorrat";
						- _name = "VorhandenerVorrat";
						- _id = GUID abc9a43b-c007-4a49-baee-c20a7f42bfc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Vorrat";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 3 1  53 1  53 19  3 19  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 43 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.000758221 524 202.844 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsCachacca.itsVorrat.VorhandenerVorrat";
					- m_csName = "Vorrat";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Abfuellstation";
							- _name = "itsVorrat";
							- _id = GUID 69d6b1ae-36e1-4768-89d5-83835f4db3c7;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsCachacca";
							- _id = GUID eafd0249-b303-4b25-82eb-c2b1ce8f1c46;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID a9757dfe-dd88-4544-95e5-6bcdabd33579;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;-2147483645;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;100;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;
";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Vorrat";
						- _name = "VorhandenerVorrat";
						- _id = GUID abc9a43b-c007-4a49-baee-c20a7f42bfc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Vorrat";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 3 1  53 1  53 19  3 19  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 43 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.000662354 601 205.738 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsEis.itsVorrat.VorhandenerVorrat";
					- m_csName = "Vorrat";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Abfuellstation";
							- _name = "itsVorrat";
							- _id = GUID 69d6b1ae-36e1-4768-89d5-83835f4db3c7;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsEis";
							- _id = GUID 59eea1c6-6535-47c5-af1f-48e41bc84559;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d8387ee0-db48-4394-9dd5-bd37e776abb5;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "digitaldisplay_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00078656 0 0 0.000278887 103 843.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[0].Brutto";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID c7ae7ff4-9680-4e54-9a0b-7c14412fd272;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "digitaldisplay_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  109 -9  109 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 296 767 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00078656 0 0 0.000278887 309 843.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[2].Brutto";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID cf12fb44-476b-46d4-abde-233b475761fc;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "digitaldisplay_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00078656 0 0 0.000278887 206 843.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[1].Brutto";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 20b54f45-5f08-431d-b1c3-c4b88133fb5f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "digitaldisplay_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  109 -9  109 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 400 763 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00078656 0 0 0.000278887 412 843.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[3].Brutto";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 64d5e2aa-7499-4562-b4ca-fd0fb5609947;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "digitaldisplay_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00078656 0 0 0.000278887 515 843.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[4].Brutto";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 95afca6e-d203-49fb-b3ee-8976f536ed13;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Waage";
						- _name = "Brutto";
						- _id = GUID 904ba2cf-7581-432e-a655-85cf92c01b3e;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "digitaldisplay_0";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  109 -9  109 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 604 760 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00078656 0 0 0.000278887 618 843.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsWaage[5].Brutto";
					- m_csName = "digitaldisplay_0";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsWaage";
							- _id = GUID 6d3a1df1-4026-4dd9-bc98-0ca3ebc05bc9;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID e3ec2e03-edcc-427b-a977-cc040142f75a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;-2147483645;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;100;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;
";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Kolben";
						- _name = "Pos";
						- _id = GUID ff98eb29-e9cc-4335-807b-6ee678c25ef2;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Schieber";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 3 1  53 1  53 19  3 19  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 43 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.000662354 347 100.738 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.itsSchieber.Pos";
					- m_csName = "Schieber";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Limetten";
							- _name = "itsSchieber";
							- _id = GUID 9b0d7d23-5bef-4820-bffc-5d9b7001481a;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 730a97ae-9c51-4b68-8847-e1e090e1b1d4;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;-2147483645;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;100;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;
";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Kolben";
						- _name = "Pos";
						- _id = GUID ff98eb29-e9cc-4335-807b-6ee678c25ef2;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Schneider";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 3 1  53 1  53 19  3 19  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 43 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.000662354 408 100.738 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.itsSchneider.Pos";
					- m_csName = "Schneider";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Limetten";
							- _name = "itsSchneider";
							- _id = GUID ebcbe5e7-d621-4869-a10e-efc1c22faaab;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 82f9cb65-5626-4daa-b78c-deb0f5cd0f17;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evFuellen()";
						- _id = GUID 23478db0-1db7-4361-a0be-dd70e7950e55;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "fuellen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  51 -9  51 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 295 313 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 388 466.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.evFuellen";
					- m_csName = "fuellen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIActiveX 
					- _id = GUID 255b5825-1592-4a35-a717-9ec076adb7b3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;DisplayedString;;Style;4;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Vorrat";
						- _name = "VorhandenerVorrat";
						- _id = GUID abc9a43b-c007-4a49-baee-c20a7f42bfc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Vorrat";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00062148 0 0 0.000278887 380 233.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.itsVorrat.VorhandenerVorrat";
					- m_csName = "Vorrat";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Abfuellstation";
							- _name = "itsVorrat";
							- _id = GUID 69d6b1ae-36e1-4768-89d5-83835f4db3c7;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID e66f90ed-e7ac-4ab7-aa2b-47642f65332e;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Limetten";
						- _name = "evNoLimette()";
						- _id = GUID 37aefd9b-cb9a-47fa-92d9-675aff0ad30d;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noLimette";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 386 581.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.evNoLimette";
					- m_csName = "noLimette";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIActiveX 
					- _id = GUID 7e22a43c-0760-44fd-aaa7-10fed55757bd;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Limetten";
						- _name = "TheLimette";
						- _id = GUID 33c6d57d-bb4f-4598-8ba8-4825280d354a;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "TheLimette";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 388 200.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.TheLimette";
					- m_csName = "TheLimette";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID ce093f67-494e-4497-a29e-ff45412cc18f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;2;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Karussell";
						- _name = "dreht";
						- _id = GUID 313e29e6-b40e-4faa-8353-705c9c0a70e8;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "dreht";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 253 224.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsKarussell.dreht";
					- m_csName = "dreht";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsKarussell";
							- _id = GUID acd87020-1336-447b-9aa9-b581bb10ef55;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID ef19efc2-8426-402d-99b0-918c9641897f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "LevelIndicator";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;-2147483645;CurrentValue;20;DrawTextLabels;-1;EnableThreshold1;-1;EnableThreshold2;-1;Font;Arial;;8.25;0;0;0;0;400;0;FormatString;%.0f;GradientFactor;0.7;HorizontalLayout;0;LiquidColor;16744576;MaximumValue;100;MinimumValue;0;NumberOfDivisions;5;NumberOfSubdivisions;1;RelativeDepth;0.2;RelativeHeight;0.9;RelativeWidth;0.9;ShadedAreaRelativeSize;0;SquareShape;0;Threshold1Color;0;Threshold1Thickness;1;Threshold1Value;75;Threshold2Color;0;Threshold2Thickness;1;Threshold2Value;35;UseColorGradients;-1;
";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 223;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Kolben";
						- _name = "Pos";
						- _id = GUID ff98eb29-e9cc-4335-807b-6ee678c25ef2;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Stampfer";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 3 1  53 1  53 19  3 19  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 291 43 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000388425 0 0 0.000758221 466 205.844 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsStampfer.itsStampferkolben.Pos";
					- m_csName = "Stampfer";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Stampfer";
							- _name = "itsStampferkolben";
							- _id = GUID fe976290-ad92-45a9-8ab0-475b8e5116d0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsStampfer";
							- _id = GUID f7c984c0-95e2-4ed7-934c-7fe70d931d1e;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID d3434b82-0383-459a-bc0a-dfff67c4ca37;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;IconSet;9;State;0;UserInteractionEnabled;-1;";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Tuer";
						- _name = "Zustand";
						- _id = GUID 73910c43-364e-4638-bce6-6cb214c1b969;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "onoff";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 455 369.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsStampfer.itsTuer.Zustand";
					- m_csName = "onoff";
					- m_PartsArray = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Station";
							- _name = "itsTuer";
							- _id = GUID 76c0e06d-2ad0-4222-b88c-3a0576999da0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsStampfer";
							- _id = GUID f7c984c0-95e2-4ed7-934c-7fe70d931d1e;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 02473b0e-0355-4c3b-9d02-9fff53637487;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;0;BlinkingTimeMillisec;300;Color;0;State;0;Style;0;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Led";
						- _name = "On";
						- _id = GUID 64444359-66bd-4d35-a057-97f287ca4fc5;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Cachacca";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 482 328.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLed[3].On";
					- m_csName = "Cachacca";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLed";
							- _id = GUID 0708781d-69fb-4775-8981-802ca12583e4;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID 20d54056-9ca3-46ac-9312-0d696f6d261a;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evFuellen()";
						- _id = GUID 23478db0-1db7-4361-a0be-dd70e7950e55;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "fuellen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 467 478.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.evFuellen";
					- m_csName = "fuellen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIMFCCtrl 
					- _id = GUID 62d2e0de-be42-4221-8627-9ca3e292e8ba;
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "evNoGlas()";
						- _id = GUID a299d62f-0336-4d8a-94b9-203f40439c92;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "noGlas";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000359293 0 0 0.000305032 468 537.34 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsLimetten.evNoGlas";
					- m_csName = "noGlas";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsLimetten";
							- _id = GUID df0f45dd-f37f-46eb-9e36-6dbbf7b7a6c0;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
					- m_csButtonCaption = "Push";
				}
				{ CGIActiveX 
					- _id = GUID 0dee5272-db01-41ec-9fa4-f3e74c78f292;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "BackColor;16777215;BlackWhenOff;0;Blinking;-1;BlinkingTimeMillisec;300;Color;2;State;0;Style;5;";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "System.sbs";
						- _subsystem = "System";
						- _class = "Station";
						- _name = "Error";
						- _id = GUID 694f5f63-4033-4697-9197-693188cd2f8c;
					}
					- m_pParent = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
					- m_name = { CGIText 
						- m_str = "Error";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 476 446.126 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Compartments = { IRPYRawContainer 
						- size = 0;
					}
					- m_csModelObjPath = "System.CaipiAutomat.itsStampfer.Error";
					- m_csName = "Error";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "Caipisystem";
							- _name = "itsStampfer";
							- _id = GUID f7c984c0-95e2-4ed7-934c-7fe70d931d1e;
						}
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "System.sbs";
							- _subsystem = "System";
							- _class = "TopLevel";
							- _name = "CaipiAutomat";
							- _id = GUID 979ab203-f577-4768-8d92-62c8cb108b33;
						}
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID ef0e94ae-5389-4d82-b25a-ceb8f70bdcab;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "System.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "System";
				- _id = GUID df584e7e-050b-41c4-88fe-3f798a129e39;
			}
		}
	}
}

