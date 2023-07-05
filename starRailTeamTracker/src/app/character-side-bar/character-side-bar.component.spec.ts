import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CharacterSideBarComponent } from './character-side-bar.component';

describe('CharacterSideBarComponent', () => {
  let component: CharacterSideBarComponent;
  let fixture: ComponentFixture<CharacterSideBarComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CharacterSideBarComponent]
    });
    fixture = TestBed.createComponent(CharacterSideBarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
