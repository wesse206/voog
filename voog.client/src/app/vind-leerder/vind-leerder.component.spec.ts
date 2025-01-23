import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VindLeerderComponent } from './vind-leerder.component';

describe('VindLeerderComponent', () => {
  let component: VindLeerderComponent;
  let fixture: ComponentFixture<VindLeerderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [VindLeerderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(VindLeerderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
